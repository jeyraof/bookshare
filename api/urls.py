# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'


from django.conf.urls import url


urlpatterns = [
    url(r'^search$', 'api.views.v1.search', name='search'),
]
