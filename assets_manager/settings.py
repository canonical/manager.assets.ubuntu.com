"""
Assets manager settings
"""
import os
import sys

SECRET_KEY = os.environ.get('SECRET_KEY', 'no_secret')

DEBUG = os.environ.get('DJANGO_DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = ['*']

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_openid_auth',
    'assets_manager',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'assets_manager.urls'
WSGI_APPLICATION = 'assets_manager.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_FINDERS = ['django_static_root_finder.finders.StaticRootFinder']

# Assets server connection
# ===
SERVER_URL = os.environ['WEBSERVICE_URL']

# You must pass the AUTH_TOKEN as an environment variable
AUTH_TOKEN = os.environ['AUTH_TOKEN']

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'dev',
        'HOST': 'db',
        'PORT': '5432',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': {
                'django.template.context_processors.request',
            },
        },
    },
]

# Update database settings from DATABASE_URL environment variable
import dj_database_url
DATABASES['default'].update(dj_database_url.config())

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = False

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'

OPENID_CREATE_USERS = True
OPENID_SSO_SERVER_URL = 'https://login.launchpad.net/'
OPENID_LAUNCHPAD_TEAMS_REQUIRED = ['canonical-content-people']
OPENID_USE_AS_ADMIN_LOGIN = True
OPENID_LAUNCHPAD_TEAMS_MAPPING_AUTO = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'error_file': {
            'level': 'WARNING',
            'filename': os.path.join(BASE_DIR, 'django-error.log'),
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1 * 1024 * 1024,
            'backupCount': 2
        }
    },
    'loggers': {
        'django': {
            'handlers': ['error_file'],
            'level': 'WARNING',
            'propagate': True
        }
    }
}
