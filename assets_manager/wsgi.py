"""
WSGI config for webapp project.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases() # noqa

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assets_manager.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402
from whitenoise.django import DjangoWhiteNoise  # noqa: E402

application = DjangoWhiteNoise(get_wsgi_application())
