# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20170510_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
