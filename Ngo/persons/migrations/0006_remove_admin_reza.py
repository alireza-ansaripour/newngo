# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_admin_reza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='reza',
        ),
    ]
