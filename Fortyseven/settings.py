"""
Django settings for Fortyseven project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see:
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# In settings.py, after initializing 'env'
ADMIN_URL = env('ADMIN_URL', default='secret-admin')


# SECURITY
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=['http://127.0.0.1'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_email_verification',
    'storages',
    'rest_framework',
    'froala_editor',
    'portfolio',
    'blogs',
]

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

# Database Configuration
if not DEBUG:
    DATABASES = {
        'default': env.db('DATABASE_URL')
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    # Alternatively, uncomment to use SQLite in development:
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static & Media Files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# CAPTCHA Configuration
GOOGLE_RECAPTCHA_SITE_KEY = env('GOOGLE_RECAPTCHA_SITE_KEY', default='dummy-site-key')
GOOGLE_RECAPTCHA_SECRET_KEY = env('GOOGLE_RECAPTCHA_SECRET_KEY', default='dummy-secret-key')

# Security Settings
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=0)
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=False)

# Email Configuration
def verified_callback(user):
    user.is_active = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_VERIFIED_CALLBACK = verified_callback

EMAIL_FROM_ADDRESS = env('EMAIL_FROM_VERIFY', default='verify@example.com')
EMAIL_FROM_RESET = env('EMAIL_FROM_RESET', default='reset@example.com')
EMAIL_MAIL_SUBJECT = env('EMAIL_MAIL_SUBJECT', default='Confirm Your Email')
EMAIL_MAIL_HTML = env('EMAIL_MAIL_HTML', default='verification-email.html')
EMAIL_MAIL_PLAIN = env('EMAIL_MAIL_PLAIN', default='mail_body.txt')
EMAIL_TOKEN_LIFE = env.int('EMAIL_TOKEN_LIFE', default=3600)
EMAIL_PAGE_TEMPLATE = env('EMAIL_PAGE_TEMPLATE', default='email-confirmation.html')
EMAIL_PAGE_DOMAIN = env('EMAIL_PAGE_DOMAIN', default='http://localhost')
EMAIL_MULTI_USER = env.bool('EMAIL_MULTI_USER', default=True)
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='your-email@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='your-email-password')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)

# AWS Configuration (For Production)
if not DEBUG:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_FILE_OVERWRITE = env.bool('AWS_S3_FILE_OVERWRITE', default=False)
    AWS_DEFAULT_ACL = None
    DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
    STATICFILES_STORAGE = env('STATICFILES_STORAGE')
    AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
    AWS_S3_SIGNATURE_VERSION = env('AWS_S3_SIGNATURE_VERSION')
    AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=525960'}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
