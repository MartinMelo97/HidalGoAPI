# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_project_laref'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='archivo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='fileRef',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]