# Generated by Django 3.2.11 on 2022-01-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scooters', '0015_auto_20220114_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='end_ride_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]