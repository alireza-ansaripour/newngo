# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20150430_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='ali',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
