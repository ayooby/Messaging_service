# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='font',
            field=models.CharField(choices=[('4x6', '4x6'), ('5x7', '5x7'), ('5x8', '5x8'), ('6x10', '6x10'), ('6x12', '6x12'), ('6x13', '6x13'), ('6x13B', '6x13B'), ('6x13O', '6x13O'), ('6x9', '6x9'), ('7x13', '7x13'), ('7x13B', '7x13B'), ('7x13O', '7x13O'), ('7x14', '7x14'), ('7x14B', '7x14B'), ('8x13', '8x13'), ('8x13B', '8x13B'), ('8x13O', '8x13O'), ('9x15', '9x15'), ('9x15B', '9x15B'), ('9x18', '9x18'), ('9x18B', '9x18B'), ('10x20', '10x20')], default='4x6', max_length=20),
        ),
    ]
