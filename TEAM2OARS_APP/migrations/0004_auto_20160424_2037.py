# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-24 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0003_auto_20160420_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_no',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]