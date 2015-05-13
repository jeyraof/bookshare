# -*- coding: utf-8 -*-

from bookshare.utils import react_render


def main(request):
    return react_render(request, 'app/main.js', {})
