# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20150430_1023'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ngo',
            field=models.ForeignKey(to='persons.NGO', default=1),
            preserve_default=False,
        ),
    ]
