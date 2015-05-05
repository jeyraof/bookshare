# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(verbose_name='\ub808\ubca8'),
        ),
        migrations.AlterModelTable(
            name='profile',
            table='user_profile',
        ),
    ]
