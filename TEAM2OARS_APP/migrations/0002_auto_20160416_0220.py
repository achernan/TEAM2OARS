# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-16 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonies',
            name='tenant_ss',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='testimonies',
            name='testimonial_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
