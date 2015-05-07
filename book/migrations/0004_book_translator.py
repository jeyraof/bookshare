# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
