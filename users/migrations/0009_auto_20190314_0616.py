# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190313_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='document',
            field=models.FileField(default='None', upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
