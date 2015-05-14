# -*- coding: utf-8 -*-

from bookshare.utils import react_render


def settings(request):
    return react_render(request, '', {})


def mail(request):
    return react_render(request, '', {})


def library(request, user_id):
    return react_render(request, '', {})


def seen(request, user_id):
    return react_render(request, '', {})


def wish(request, user_id):
    return react_render(request, '', {})
