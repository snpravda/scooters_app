# Generated by Django 3.2.11 on 2022-01-11 21:20

from django.db import migrations, models
import scooters.models


class Migration(migrations.Migration):

    dependencies = [
        ('scooters', '0009_remove_scooter_used_by_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='scooter',
            name='used_by_user',
            field=models.IntegerField(default=None, verbose_name=scooters.models.User),
            preserve_default=False,
        ),
    ]
