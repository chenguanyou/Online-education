# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 00:52
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20180107_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coures',
            name='detail',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='课程详情'),
        ),
    ]
