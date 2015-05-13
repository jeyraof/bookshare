# -*- coding: utf-8 -*-

from django.conf.urls import url
from book.views import BookDetail


urlpatterns = [
    url(r'^(\d+)$', BookDetail.as_view(), name='detail'),
    url(r'^search$', 'book.views.search_books', name='search'),
    url(r'^recent$', BookDetail.as_view(), name='recent'),
    url(r'^available$', BookDetail.as_view(), name='available'),
]
