# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-13 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190313_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='None', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='plan',
            field=models.CharField(choices=[('Free', 'Free'), ('Pro', 'Pro - $9.99/mo')], default='None', max_length=1),
            preserve_default=False,
        ),
    ]
