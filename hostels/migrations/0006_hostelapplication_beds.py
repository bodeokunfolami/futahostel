# Generated by Django 4.1.6 on 2023-02-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0005_hostel_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelapplication',
            name='beds',
            field=models.PositiveIntegerField(default=1),
        ),
    ]