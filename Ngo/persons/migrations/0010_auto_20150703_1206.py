# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0009_auto_20150528_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='flag',
            field=models.FileField(upload_to='/home/alireza/PycharmProjects/newngo/media', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ngo',
            name='continent',
            field=models.CharField(choices=[('as', 'آسیا'), ('er', 'اروپا'), ('am', 'آمریکا'), ('au', 'استرالیا و اقیانوسیه'), ('af', 'آفریقا')], max_length=2),
            preserve_default=True,
        ),
    ]
