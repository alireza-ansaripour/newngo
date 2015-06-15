# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='flag',
        ),
        migrations.AddField(
            model_name='ngo',
            name='latin_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
