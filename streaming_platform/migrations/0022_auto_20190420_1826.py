# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0021_movie_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='bio',
            new_name='summary',
        ),
    ]
