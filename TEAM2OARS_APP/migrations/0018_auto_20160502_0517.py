# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-02 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0017_auto_20160502_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='employer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='tenant_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='tenant_ss',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]
