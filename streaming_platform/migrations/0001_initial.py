# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('year', models.DateField()),
                ('video_url', models.URLField()),
            ],
        ),
    ]