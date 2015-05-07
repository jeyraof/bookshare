# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20150507_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumb',
            field=models.CharField(max_length=255, blank=1),
        ),
    ]
