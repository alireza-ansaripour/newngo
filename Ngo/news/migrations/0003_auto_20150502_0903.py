# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_admin_reza'),
        ('news', '0002_news_ngo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='ngo',
            field=models.ForeignKey(default=1, to='persons.NGO'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='text',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]
