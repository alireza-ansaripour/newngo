# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'کارشناسان',
                'verbose_name': 'کارشناس',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('continent', models.CharField(choices=[('as', 'آسیا'), ('er', 'اروپا'), ('am', 'آمریکا'), ('au', 'استرالیا و اقیانوسیه'), ('af', 'آفریقا')], max_length=2)),
                ('Website', models.CharField(max_length=50)),
                ('flag', models.FileField(upload_to='/root/PycharmProjects/Ngo/src/../media')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expert',
            name='ngo',
            field=models.ForeignKey(to='persons.NGO'),
            preserve_default=True,
        ),
    ]
