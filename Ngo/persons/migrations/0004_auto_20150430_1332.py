# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_expert_ali'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ngo',
            name='history',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
