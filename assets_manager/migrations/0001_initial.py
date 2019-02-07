# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()  # noqa

from django.db import migrations
from django.contrib.auth.models import Group


def create_groups(apps, schema_editor):
    authors = Group(name="canonical-content-people")
    authors.save()


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0001_initial"),
        ("django_openid_auth", "0001_initial"),
    ]
    operations = [migrations.RunPython(create_groups)]
