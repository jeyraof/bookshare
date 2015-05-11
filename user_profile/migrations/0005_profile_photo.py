# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20150509_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
