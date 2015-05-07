# -*- coding: utf-8 -*-

from django.conf.urls import url
from book.views import BookDetail


urlpatterns = [
    url(r'^$', BookDetail.as_view()),
]
