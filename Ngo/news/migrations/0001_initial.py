# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('continent', models.CharField(choices=[('as', 'آسیا'), ('er', 'اروپا'), ('am', 'آمریکا'), ('au', 'استرالیا و اقیانوسیه'), ('af', 'آفریقا')], max_length=2)),
                ('status', models.CharField(choices=[('n', 'نامشخص'), ('i', 'مهم'), ('r', 'معمولی')], default='n', max_length=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('description', models.CharField(max_length=100)),
                ('title_image', models.FileField(upload_to='/root/PycharmProjects/Ngo/src/../media')),
                ('random_int', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('pic', models.FileField(upload_to='/root/PycharmProjects/Ngo/src/../media')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(to='news.News'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='comment',
            field=models.ForeignKey(to='news.Comment'),
            preserve_default=True,
        ),
    ]
