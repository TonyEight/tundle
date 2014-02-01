# -*- coding: utf-8 -*-

"""
Base settings for tundle project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

import os

# We get the path of all this directories from the "path" module. The path.py
# file is a module coded by SamEtMax, it's not provided by Django, but it's
# very useful to avoid hard coding all these paths.
from tundle.path import PROJECT_DIR, ROOT_DIR, TEMP_DIR, APPS_DIR


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')ifl28!y1n+uwvkoz*@@$wtwu1#+r$$1d7dnld2bqpyb%l1$lb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tundle.urls'

WSGI_APPLICATION = 'tundle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Django uses the Python log standard facility, and this dictionary is passed
# to dictConfig (http://docs.python.org/2/library/logging.config.html).
# This one allows you to log to the console
# and a file in temp dir.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { # what to dump in each log
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': { # mandatory since django 1.5
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': { # send a mail to admins
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{ # print on the console
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file':{ # write in a temp file
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(TEMP_DIR, 'project.django.log'),
            'maxBytes': 1000000,
            'backupCount': 1,
        },
    },
    'loggers': {
        'django.request': { # send an email to admins if a request fails
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.project': { # write manually to the console and the tempfile
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
