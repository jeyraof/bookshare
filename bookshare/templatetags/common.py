# -*- coding: utf-8 -*-


from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='node_module')
def make_node_module(file_path):
    return settings.NODE_MODULES_URL + file_path
