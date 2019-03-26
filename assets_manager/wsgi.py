"""
WSGI config for webapp project.
"""

# Standard library
import os

# Packages
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assets_manager.settings")
application = get_wsgi_application()
