# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_remove_expert_ali'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='country',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
