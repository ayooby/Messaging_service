# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import map.models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20160921_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='mapname',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='picture',
            field=models.FileField(upload_to=map.models.content_file_name),
        ),
    ]
