# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_ngo_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='continent',
            field=models.CharField(choices=[('as', 'آسیا'), ('eu', 'اروپا'), ('am', 'آمریکا'), ('au', 'استرالیا و اقیانوسیه'), ('af', 'آفریقا')], max_length=2),
            preserve_default=True,
        ),
    ]
