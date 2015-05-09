# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='stock',
        ),
        migrations.AddField(
            model_name='library',
            name='available',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='library',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'have'), (1, b'rental')]),
        ),
    ]
