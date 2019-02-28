# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0006_auto_20190227_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='TV_channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('currently_streaming', models.CharField(max_length=200)),
                ('live', models.BooleanField()),
            ],
        ),
    ]
