"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import ungettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
from django.utils.translation import gettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm*dr6has)&_xkt$v$6-kv7bm939&iux^^gcwc*_#cju@xz9*c1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration.apps.RegistrationConfig',
    'zad.apps.ZadConfig',
    'rest_framework',
    'api.apps.ApiConfig',

]

'''MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]'''
MIDDLEWARE = [

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

                #' django.template.context_processors.i18n',



            ],
        },
    },
]


        #'DIRS': [os.path.join(BASE_DIR, "templates/")],

LOCALE_PATHS = (

    os.path.join(BASE_DIR, 'locale'),

)

WSGI_APPLICATION = 'mysite.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases



#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ar-ae'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
_ = lambda s: s



STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rababalesead12@gmail.com'
EMAIL_HOST_PASSWORD = 'tobeornottobe'

#DEFAULT_FROM_EMAIL = 'rababkhalifamohammed@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
#EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
#ADMINS = (('rabab','rababkhalifamohammed@gmail.com'),)
#MANAGERS=ADMINS;



LANGUAGES = (
    ('ar', _('Arabic')),
    ('en', _('English')),
)

MULTILINGUAL_LANGUAGES = (
    "en-us",
    "ar-ae",
)

AUTH_USER_MODEL = 'registration.Account'
