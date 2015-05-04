# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%)on^uto7hereohw55y0mmze@fanuc_)gsur3%kks6eve4lt$l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
