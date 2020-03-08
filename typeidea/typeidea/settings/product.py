# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '172.81.211.221',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'lbs19940529',
        'PORT': 3306,
        # 'TEST': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://5623064@172.81.211.221:6379/10',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        }
    }
}

# INSTALLED_APPS += [
    # 'debug_toolbar',
    # 'silk',
# ]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware',
# ]

# INTERNAL_IPS = ['127.0.0.1']