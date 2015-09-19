# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_photo_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(to='news.News', related_name='comments'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('n', 'نامشخص'), ('i', 'مهم'), ('r', 'معمولی'), ('a', 'آرشیو')], max_length=1, default='n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title_image',
            field=models.FileField(upload_to='/home/alireza/PycharmProjects/newngo/media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='pic',
            field=models.FileField(upload_to='/home/alireza/PycharmProjects/newngo/media'),
            preserve_default=True,
        ),
    ]
