# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-07 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20170422_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='netid',
            field=models.CharField(default='netid', max_length=100),
            preserve_default=False,
        ),
    ]