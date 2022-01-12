# Generated by Django 3.2.11 on 2022-01-11 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('price_per_hour', models.FloatField(verbose_name='price_per_hour')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Scooter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('battery_percentage', models.IntegerField(verbose_name='battery_percentage')),
                ('is_free', models.BooleanField(default=True, verbose_name='is_free')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scooters.provider')),
            ],
        ),
    ]
