# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-02 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0020_auto_20160502_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant_family',
            name='child',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tenant_family',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tenant_family',
            name='spouse',
            field=models.CharField(max_length=50),
        ),
    ]
