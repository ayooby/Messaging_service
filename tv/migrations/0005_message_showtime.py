# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 10:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0004_auto_20161212_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='showtime',
            field=models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
