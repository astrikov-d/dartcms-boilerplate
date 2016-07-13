# coding: utf-8
# Project and environment specific settings.
APP_DOMAIN = 'example.com'
APP_URL = 'http://%s:8000' % APP_DOMAIN

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'boilerplate',
        'USER': 'boilerplate',
        'PASSWORD': '37FgH1zM',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
