# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(u'레벨')

    class Meta:
        db_table = 'user_profile'


class Library(models.Model):
    # Constants
    STATUS_HAVE = (0, 'have')
    STATUS_RENTAL = (1, 'rental')

    # Columns
    user = models.ForeignKey(User, db_index=1)
    book = models.ForeignKey('book.Book', db_index=1)
    available = models.BooleanField(default=0)
    status = models.IntegerField(choices=(STATUS_HAVE,
                                          STATUS_RENTAL),
                                 default=STATUS_HAVE[0])

    @classmethod
    def add(cls, user, book):
        if not user or not book:
            return None

        lib = cls(user=user, book=book)
        lib.save()
        return lib

    def remove(self):
        self.delete()

    class Meta:
        db_table = 'user_library'
