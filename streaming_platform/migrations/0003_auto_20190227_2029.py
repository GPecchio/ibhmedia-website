# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0002_auto_20190227_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(),
        ),
    ]
