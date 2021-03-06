# Generated by Django 2.0 on 2018-01-17 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0027_auto_20180108_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCUAGenerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_creation', models.DateField(auto_now_add=True)),
                ('record_update', models.DateField(auto_now=True)),
                ('ticket', models.CharField(blank=True, max_length=12, null=True, verbose_name='SN Ticket')),
                ('startdate', models.CharField(default='01/17/2018', max_length=32, verbose_name='Start Date')),
                ('enddate', models.CharField(default='01/17/2019', max_length=32, verbose_name='End Date')),
                ('folder1', models.CharField(default='dcore-prj00XX-SOURCE', max_length=128, verbose_name='Folder 1')),
                ('folder2', models.CharField(blank=True, default='dcore-prj00XX-SHARE', max_length=128, null=True, verbose_name='Folder 2')),
                ('folder3', models.CharField(blank=True, default='WorkArea-<user CWID>', max_length=128, null=True, verbose_name='Folder 3')),
                ('folder4', models.CharField(blank=True, max_length=128, null=True, verbose_name='Folder 4')),
                ('folder5', models.CharField(blank=True, max_length=128, null=True, verbose_name='Folder 5')),
                ('folder6', models.CharField(blank=True, max_length=128, null=True, verbose_name='Folder 6')),
                ('folder7', models.CharField(blank=True, max_length=128, null=True, verbose_name='Folder 7')),
                ('url', models.CharField(blank=True, max_length=512, null=True, verbose_name='Qualtrics URL')),
            ],
        ),
        migrations.AddField(
            model_name='softwarecost',
            name='cost_classroom',
            field=models.FloatField(blank=True, null=True, verbose_name='Cost for classrooms (per student)'),
        ),
        migrations.AddField(
            model_name='softwarecost',
            name='cost_student',
            field=models.FloatField(blank=True, null=True, verbose_name='Cost for classrooms (per class)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='backup_storage',
            field=models.IntegerField(blank=True, null=True, verbose_name='Backup storage size (GB)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='direct_attach_storage',
            field=models.IntegerField(blank=True, null=True, verbose_name='Direct attach size (GB)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='env_type',
            field=models.CharField(choices=[('TH', 'Thesis Project'), ('RE', 'Research Project'), ('CL', 'Classroom Project')], default='RE', max_length=2, verbose_name='Environment type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fileshare_storage',
            field=models.IntegerField(blank=True, null=True, verbose_name='Fileshare size (GB)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='requested_ram',
            field=models.IntegerField(blank=True, null=True, verbose_name='Requested RAM (GB)'),
        ),
        migrations.AlterField(
            model_name='softwarecost',
            name='software_cost',
            field=models.FloatField(blank=True, null=True, verbose_name='Regular cost (per person)'),
        ),
        migrations.AddField(
            model_name='dcuagenerator',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dc_management.Project'),
        ),
    ]
