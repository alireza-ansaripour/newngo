# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_remove_admin_reza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='ali',
        ),
    ]
