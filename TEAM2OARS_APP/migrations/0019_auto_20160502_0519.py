# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-02 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0018_auto_20160502_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobiles',
            name='auto_color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='automobiles',
            name='auto_make',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='automobiles',
            name='auto_year',
            field=models.CharField(max_length=4),
        ),
    ]
