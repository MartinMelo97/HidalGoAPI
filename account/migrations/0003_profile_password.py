# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161017_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
