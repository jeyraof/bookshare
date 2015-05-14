# -*- coding: utf-8 -*-

from bookshare.utils import react_render


def search(request):
    return react_render(request, 'app/search.js', {
        'search_keyword': request.GET.get('q', u'')
    })
