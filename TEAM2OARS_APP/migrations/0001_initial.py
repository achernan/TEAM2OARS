# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-16 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('testimonial_id', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('testimonial_date', models.DateField()),
                ('testimonial_content', models.TextField()),
                ('tenant_ss', models.IntegerField(max_length=9)),
            ],
        ),
    ]
