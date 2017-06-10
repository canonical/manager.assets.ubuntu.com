"""
WSGI config for webapp project.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assets_manager.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402
from whitenoise.django import DjangoWhiteNoise  # noqa: E402

application = DjangoWhiteNoise(get_wsgi_application())
