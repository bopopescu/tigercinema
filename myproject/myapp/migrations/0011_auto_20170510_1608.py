# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 16:08
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20170509_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]
