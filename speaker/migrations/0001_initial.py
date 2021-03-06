# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import speaker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('filename', models.FileField(upload_to=speaker.models.content_file_name)),
            ],
        ),
    ]
