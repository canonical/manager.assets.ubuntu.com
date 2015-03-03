# Third party imports
from django.conf.urls import patterns, url
from django.contrib import admin

# Local imports
from views import index, create, update, error_404

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^create$', create, name='create'),
    url(r'^update$', update, name='update'),
)

handler404 = error_404
