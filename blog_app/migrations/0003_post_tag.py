# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]