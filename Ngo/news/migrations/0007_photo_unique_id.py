# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150528_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='unique_id',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
