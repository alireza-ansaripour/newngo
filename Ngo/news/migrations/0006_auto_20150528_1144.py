# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150504_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='continent',
            field=models.CharField(choices=[('as', 'آسیا'), ('eu', 'اروپا'), ('am', 'آمریکا'), ('au', 'استرالیا و اقیانوسیه'), ('af', 'آفریقا')], max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='random_int',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
