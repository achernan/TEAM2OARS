# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0007_auto_20160424_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonies',
            name='testimonial_id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
