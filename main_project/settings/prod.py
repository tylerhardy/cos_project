# -*- coding: utf-8 -*- 
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '137.190.117.94','ty128-rpi3.users.weber.edu']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cos_dev_db',
        'USER': 'tylerhardy',
        'PASSWORD': 'Letmein11',
        'HOST': 'localhost',
        'PORT': '',
    }
}
