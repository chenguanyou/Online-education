# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile_is_jh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_jh',
            field=models.IntegerField(choices=[('1', '激活'), ('0', '未激活')], default='1', verbose_name='是否激活'),
        ),
    ]
