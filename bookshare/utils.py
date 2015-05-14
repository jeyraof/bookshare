# -*- coding: utf-8 -*-

from django.core import serializers
from django.shortcuts import render


def react_render(request, script_path, context=None):
    ctx = {'script_path': script_path}
    if isinstance(context, dict):
        ctx.update(context)

    return render(request=request,
                  template_name='react.render.html',
                  context=ctx)


def serialize(obj_list):
    if not obj_list:
        return u''

    obj = obj_list if isinstance(obj_list, list) else [obj_list, ]
    serialized_data = serializers.serialize('json', obj)
    return serialized_data
