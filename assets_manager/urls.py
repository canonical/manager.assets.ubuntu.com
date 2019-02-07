from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()  # noqa

# Third party imports
from django.conf.urls import url, include
from django.contrib import admin

# Local imports
from .views import index, create, update, error_404

admin.autodiscover()

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^create$", create, name="create"),
    url(r"^update$", update, name="update"),
    url(r"^openid/", include("django_openid_auth.urls")),
]

handler404 = error_404
