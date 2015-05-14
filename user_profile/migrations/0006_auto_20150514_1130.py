# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.CharField(default=b'', max_length=255, verbose_name='\ud504\ub85c\ud544\uc0ac\uc9c4'),
        ),
    ]
