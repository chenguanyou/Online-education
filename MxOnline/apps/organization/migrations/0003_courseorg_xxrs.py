# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20171230_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='xxrs',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]