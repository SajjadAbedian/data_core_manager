# Generated by Django 2.0 on 2018-01-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0025_project_backup_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_total_cost',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
