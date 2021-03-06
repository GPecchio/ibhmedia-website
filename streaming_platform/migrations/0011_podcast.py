# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0010_auto_20190227_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=8)),
                ('release_date', models.DateField()),
                ('url', models.URLField()),
                ('slug', models.SlugField(default='not_found')),
            ],
        ),
    ]
