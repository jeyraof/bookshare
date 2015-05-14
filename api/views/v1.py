# -*- coding: utf-8 -*-

from django.db.models import Q
from django.http import (JsonResponse, HttpResponseBadRequest)
from book.models import Book
from bookshare.utils import serialize, paginate


def search(request):
    q = request.GET.get('q', None)
    if not q:
        return HttpResponseBadRequest(u'인자가 부족합니다.')

    page, book_a, book_z = paginate(request.GET, Book.SEARCH_COUNT)

    books = Book.objects\
                .filter(Q(author__contains=q) |
                        Q(title__contains=q) |
                        Q(isbn=q))\
                .order_by('-created_at')[book_a:book_z]

    if books.exists():
        item = books
    else:
        item = Book.search(search_type='all',
                           q=q,
                           embago=Book.SEARCH_COUNT,
                           page=page)

    return JsonResponse({
        'ok': 1,
        'item': serialize(item),
        'page': int(page),
        'q': q,
    })
