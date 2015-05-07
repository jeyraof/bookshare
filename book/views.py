# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class BookDetail(TemplateView):
    template_name = 'book/detail.html'

    def get(self, request, *args, **kwargs):
        return super(BookDetail, self).get(request, *args, **kwargs)
