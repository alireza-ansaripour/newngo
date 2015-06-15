# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_remove_admin_reza'),
        ('news', '0004_auto_20150502_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='ngo',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.AddField(
            model_name='photo',
            name='ngo',
            field=models.ForeignKey(default=1, to='persons.NGO'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='text',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
