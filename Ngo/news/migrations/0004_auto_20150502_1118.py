# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_admin_reza'),
        ('news', '0003_auto_20150502_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(upload_to='/root/PycharmProjects/Ngo/src/../media')),
                ('text', models.CharField(max_length=100)),
                ('ngo', models.ForeignKey(to='persons.NGO')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='photo',
            name='ngo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text',
        ),
    ]
