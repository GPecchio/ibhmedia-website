# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190314_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='document',
            field=models.FileField(upload_to='media/'),
        ),
    ]