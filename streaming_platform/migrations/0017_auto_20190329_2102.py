# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-30 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0016_auto_20190329_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='videofile',
            new_name='video_file',
        ),
    ]