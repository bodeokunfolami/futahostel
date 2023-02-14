# Generated by Django 4.1.6 on 2023-02-14 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0002_rename_rooms_hostel_beds_remove_hostel_slug_and_more'),
        ('users', '0002_studentprofile_matric_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='department',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='status',
            field=models.CharField(choices=[('N', 'No Appplication'), ('P', 'Pending'), ('C', 'Complete'), ('R', 'Rejected')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='hostel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostels.hostel'),
        ),
    ]
