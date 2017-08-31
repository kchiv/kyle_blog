# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 23:36
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('posts', '0002_auto_20170829_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_featured_image', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_featured_image', to='filer.Image'),
        ),
    ]