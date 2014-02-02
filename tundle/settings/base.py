# coding=utf-8

"""Base settings for tundle project.

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
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'south',
    'timedelta',
    # Tundle apps
    'demands',
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
STATIC_ROOT = os.path.join(PROJECT_DIR, 'assets/static')

# Users-uploaded files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'assets/media')

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

# Attachments app settings
# List of allowed types (MIME types).
ATTACHMENT_CONTENT_TYPES = [
    'application/pdf', 
    'application/zip',
    'application/vnd.oasis.opendocument.text',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.oasis.opendocument.presentation',
    'application/vnd.oasis.opendocument.graphics',
    'text/csv',
    'text/html',
    'text/plain',
    'application/msword',
    'application/msword',
    'application/vnd.openxmlformats-officedocument'
    '.wordprocessingml.document',
    'application/vnd.openxmlformats-officedocument'
    '.wordprocessingml.template',
    'application/vnd.ms-word.document.macroEnabled.12',
    'application/vnd.ms-word.template.macroEnabled.12',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument'
    '.spreadsheetml.sheet',
    'application/vnd.openxmlformats-officedocument'
    '.spreadsheetml.template',
    'application/vnd.ms-excel.sheet.macroEnabled.12',
    'application/vnd.ms-excel.template.macroEnabled.12',
    'application/vnd.ms-excel.addin.macroEnabled.12',
    'application/vnd.ms-excel.sheet.binary.macroEnabled.12',
    'application/vnd.ms-powerpoint',
    'application/vnd.openxmlformats-officedocument'
    '.presentationml.presentation',
    'application/vnd.openxmlformats-officedocument'
    '.presentationml.template',
    'application/vnd.openxmlformats-officedocument'
    '.presentationml.slideshow',
    'application/vnd.ms-powerpoint.addin.macroEnabled.12',
    'application/vnd.ms-powerpoint.presentation.macroEnabled.12',
    'application/vnd.ms-powerpoint.template.macroEnabled.12',
    'application/vnd.ms-powerpoint.slideshow.macroEnabled.12',
    'image/gif',
    'image/jpeg',
    'image/pjpeg',
    'image/png',
    'image/x-png',
    'image/tiff',
    'image/svg+xml',
]

# This setting fixes the max size of an attachment
# Here are some size examples
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 52428800
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
ATTACHMENT_MAX_SIZE = 10485760
