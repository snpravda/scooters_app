# Generated by Django 3.2.11 on 2022-01-11 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scooters', '0007_auto_20220111_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scooter',
            name='used_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scooters.user'),
        ),
    ]