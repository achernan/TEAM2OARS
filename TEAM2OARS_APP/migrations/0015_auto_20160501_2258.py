# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-01 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0014_auto_20160501_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apt_no',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
