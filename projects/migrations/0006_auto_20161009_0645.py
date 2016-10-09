# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 11:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20161009_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='projects.Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]