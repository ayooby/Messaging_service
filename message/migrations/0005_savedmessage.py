# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20161204_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('jsonlist', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
        ),
    ]
