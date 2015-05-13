# -*- coding: utf-8 -*-

from django.shortcuts import render


def react_render(request, script_path, context=None):
    ctx = {'script_path': script_path}
    if isinstance(context, dict):
        ctx.update(context)

    return render(request=request,
                  template_name='react.render.html',
                  context=ctx)
