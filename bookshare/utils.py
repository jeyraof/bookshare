# -*- coding: utf-8 -*-

from django.core import serializers
from django.shortcuts import render
import json


def react_render(request, script_path, context=None):
    ctx = {'script_path': script_path}
    if isinstance(context, dict):
        ctx.update(context)

    return render(request=request,
                  template_name='react.render.html',
                  context=ctx)


def serialize(obj_list):
    serialized_data = serializers.serialize('json', obj_list)
    return json.loads(serialized_data)


def paginate(d, embago=20):
    page_now = int(d.get('page', 1))
    item_init = (page_now - 1) * embago
    item_end = item_init + embago
    return page_now, item_init, item_end
