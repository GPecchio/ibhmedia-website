# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0020_auto_20190418_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='bio',
            field=models.TextField(default='not found', max_length=300),
        ),
    ]
