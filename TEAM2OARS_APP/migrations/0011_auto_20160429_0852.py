# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-29 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TEAM2OARS_APP', '0010_auto_20160424_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='tenant_ss',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='tenant_ss',
        ),
        migrations.RemoveField(
            model_name='handle_rents',
            name='complaint_no',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='tenant_ss',
        ),
        migrations.AddField(
            model_name='complaints',
            name='apt_no',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='TEAM2OARS_APP.Apartment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaints',
            name='rental_no',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='TEAM2OARS_APP.Handle_Rents'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='handle_rents',
            name='apt_no',
            field=models.ForeignKey(default=333, on_delete=django.db.models.deletion.CASCADE, to='TEAM2OARS_APP.Apartment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoices',
            name='rental_no',
            field=models.ForeignKey(default=222, on_delete=django.db.models.deletion.CASCADE, to='TEAM2OARS_APP.Handle_Rents'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='rental_no',
            field=models.ForeignKey(default=444, on_delete=django.db.models.deletion.CASCADE, to='TEAM2OARS_APP.Handle_Rents'),
            preserve_default=False,
        ),
    ]
