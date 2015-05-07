# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(u'레벨')

    class Meta:
        db_table = 'user_profile'


class Library(models.Model):
    user = models.ForeignKey(User, db_index=1)
    book = models.ForeignKey('book.Book', db_index=1)
    stock = models.IntegerField(default=1)

    class Meta:
        db_table = 'user_library'
