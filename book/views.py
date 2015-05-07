# -*- coding: utf-8 -*-

from django.http import (JsonResponse,
                         HttpResponseNotAllowed, HttpResponseBadRequest)
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from book.models import Book


class BookDetail(TemplateView):
    template_name = 'book/detail.html'

    def get(self, request, *args, **kwargs):
        return super(BookDetail, self).get(request, *args, **kwargs)


@csrf_exempt
def search_books(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(u'잘못된 접근입니다.')

    q = request.POST.get('q', None)
    if not q:
        return HttpResponseBadRequest(u'인자가 부족합니다.')

    search_type = request.POST.get('type', 'all')
    books = Book.search(search_type=search_type,
                        q=q)
    return JsonResponse({'books': map(lambda b: b.to_json(), books)})
