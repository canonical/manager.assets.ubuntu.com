"""
Assets manager settings
"""

# Keep it secret, keep it safe!
# Although it probably doesn't matter for this app...
SECRET_KEY = '3z7qsr3n^@dhyb3qh_x_1c#6of_^d=uovy+a7)9sst))ns(697'

ALLOWED_HOSTS = [
    '0.0.0.0', '127.0.0.1', 'localhost',
    '*.ubuntu.qa', '*.ubuntu.com', 'ubuntu.com'
]

# Application definition
INSTALLED_APPS = []
MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'assets_manager.urls'
WSGI_APPLICATION = 'assets_manager.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = ["static"]
TEMPLATE_DIRS = ["templates"]
TEMPLATE_CONTEXT_PROCESSORS = ['django.core.context_processors.request']

# Assets server connection
# ===
import os

AUTH_TOKEN = '<TOKEN_PLACEHOLDER>'
SERVER_URL = os.environ.get(
    'WEBSERVICE_URL',
    'http://localhost:8001'
)
