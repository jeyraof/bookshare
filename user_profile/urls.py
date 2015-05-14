# -*- coding: utf-8 -*-

from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<user_id>\d+)/library$', 'user_profile.views.library', name='library'),  # 책장
    url(r'^(?P<user_id>\d+)/seen$', 'user_profile.views.seen', name='seen'),     # 본 책
    url(r'^(?P<user_id>\d+)/wish$', 'user_profile.views.wish', name='wish'),     # 보고싶은 책
]
