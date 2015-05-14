# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_translator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 14, 2, 30, 3, 358414, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
