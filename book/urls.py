# -*- coding: utf-8 -*-

from django.conf.urls import url


urlpatterns = [
    url(r'^(\d+)$', 'book.views.search', name='detail'),
    url(r'^search$', 'book.views.search', name='search'),
    url(r'^recent$', 'book.views.search', name='recent'),
    url(r'^available$', 'book.views.search', name='available'),
]
