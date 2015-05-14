# -*- coding: utf-8 -*-

from django.db.models import Q
from django.http import (JsonResponse, HttpResponseBadRequest)
from book.models import Book
from bookshare import utils


def search(request):
    q = request.GET.get('q', None)
    if not q:
        return HttpResponseBadRequest(u'인자가 부족합니다.')

    page, book_a, book_z = utils.paginate(request.GET, 20)

    books_db = Book.objects\
                   .filter(Q(author__contains=q) |
                           Q(title__contains=q) |
                           Q(isbn=q))\
                   .order_by('-created_at')[book_a:book_z]

    books_daum = []
    if request.GET.get('daum', False):
        books_daum = Book.search(search_type='all', q=q)

    return JsonResponse({
        'ok': 1,
        'msg': u'',
        'item': {
            'db': utils.serialize(books_db),
            'daum': utils.serialize(books_daum),
        }
    })
