# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapname', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='map/static/map/pictures/')),
                ('markers', jsonfield.fields.JSONField()),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Floor')),
            ],
        ),
    ]
