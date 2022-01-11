# Generated by Django 3.2.11 on 2022-01-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scooters', '0003_scooter_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='scooter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
