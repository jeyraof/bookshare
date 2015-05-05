# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(u'레벨')

    class Meta:
        db_table = 'user_profile'
