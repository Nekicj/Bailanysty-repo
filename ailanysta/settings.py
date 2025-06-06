"""
Django settings for ailanysta project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os 
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from dotenv import load_dotenv
load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i%q$3y*i83qi2ctv57jt230^e(&3m*___*jz%hrj9khs^+cxsx'

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
    'posts',
    'users',
    'rest_framework',
    'notifications',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
    
]

ROOT_URLCONF = 'ailanysta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  
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

WSGI_APPLICATION = 'ailanysta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'Bailanysty',
#        'USER': 'postgres',
#        'PASSWORD': 'csgolox13',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}
# BBEEBEE

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

import dj_database_url


#POSTGRES_LOCALLY = True
#DATABASES = {
#    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
#}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


AUTH_USER_MODEL = 'users.CustomUser'
 
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

LOGOUT_REDIRECT_URL = '/accounts/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#if DEBUG:
#    CSRF_COOKIE_SECURE = False
#    CSRF_COOKIE_HTTPONLY = False
#    CSRF_USE_SESSIONS = False
#else:
#    CSRF_COOKIE_SECURE = True
#    CSRF_COOKIE_HTTPONLY = True
#    CSRF_USE_SESSIONS = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True

CORS_ALLOW_ALL_ORIGINS = True
#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:8000",
#    "http://127.0.0.1:8000",
#    'bailanysty.up.railway.app',
#]
CORS_ALLOWED_ORIGINS = []
CSRF_TRUSTED_ORIGINS = ['https://*', 'http://*',"https://bailanysty.up.railway.app"]

# Default profile image - relative to MEDIA_ROOT
DEFAULT_PROFILE_IMAGE = 'profiles/default_profile.png'
