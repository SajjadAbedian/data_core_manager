# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0006_auto_20170922_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='access_log',
            name='prj_affected',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dc_management.Project'),
            preserve_default=False,
        ),
    ]
