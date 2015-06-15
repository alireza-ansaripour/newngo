# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20150430_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='reza',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
