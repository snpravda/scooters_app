from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField("id", primary_key=True)
    email = models.EmailField("email", unique=True)

    def __str__(self):
        return self.email


class Provider(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("name", max_length=30)
    price_per_hour = models.FloatField("price_per_hour")

    def __str__(self):
        return self.name


class Scooter(models.Model):
    id = models.AutoField("id", primary_key=True)
    latitude = models.FloatField("latitude")
    longitude = models.FloatField("longitude")
    battery_percentage = models.IntegerField("battery_percentage")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    used_by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"location: {self.latitude}, {self.longitude}; provider: {self.provider.name}"
