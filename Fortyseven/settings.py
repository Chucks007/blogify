"""
Django settings for Fortyseven project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fe1#n^faux117p6=ip64q0%)f1^6sb3sdw6&2&1b)w77ho3nfy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_email_verification',
    'rest_framework',
    'captcha',
    'froala_editor',
    'portfolio',
    'blogs'
]

CSRF_TRUSTED_ORIGINS = ['https://*.ngrok.io','https://*.127.0.0.1']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Fortyseven.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "template"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Fortyseven.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / "static"]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# RECAPTCHA V2 API KEYS
# RECAPTCHA_PUBLIC_KEY = '6LcfJ_seAAAAAE7OAnqMkgRa4ieOcJDz1cXq8eV3'
# RECAPTCHA_PRIVATE_KEY = '6LcfJ_seAAAAANzljZnoQpTk4SKGxsZTm6JV5pgc'
# RECAPTCHA_REQUIRED_SCORE = 0.85


GOOGLE_RECAPTCHA_SITE_KEY = '6Lf8ZAUfAAAAADLG4s-ANbIJDi-B-5vNixRgIyc8' #your reCAPTCHA SITE key 
GOOGLE_RECAPTCHA_SECRET_KEY = '6Lf8ZAUfAAAAAMWYF4ftGuHuSoATYV7Bmz8rDfxh' #your reCAPTCHA SECRET key 
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


def verified_callback(user):
    user.is_active = True

EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = '0a000047@gmail.com' 
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'mail_body.html'
EMAIL_MAIL_PLAIN = 'mail_body.txt'
EMAIL_TOKEN_LIFE = 60 * 60
EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'
EMAIL_MULTI_USER = True  # optional (defaults to False)

# For Django Email Backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '0a000047@gmail.com'
EMAIL_HOST_PASSWORD = '511750#21104041'  # os.environ['password_key'] suggested
EMAIL_USE_TLS = True