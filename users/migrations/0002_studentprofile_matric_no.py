# Generated by Django 4.1.6 on 2023-02-12 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='matric_no',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
