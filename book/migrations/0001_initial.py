# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=30, db_index=1)),
                ('title', models.CharField(max_length=255, db_index=1)),
                ('publisher', models.CharField(max_length=50, db_index=1)),
                ('category', models.CharField(max_length=50, db_index=1)),
            ],
        ),
    ]
