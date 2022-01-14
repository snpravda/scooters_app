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
    provider: Provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    used_by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    last_ride: "Ride" = models.ForeignKey(
        "Ride", on_delete=models.CASCADE, null=True, blank=True, related_name="scooter_ride")

    def __str__(self):
        return f"location: {self.latitude}, {self.longitude}; provider: {self.provider.name}"


class Ride(models.Model):
    id = models.AutoField("id", primary_key=True)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    scooter: Scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
    start_ride_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_ride_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"user_id: {self.user.id}, scooter_id: {self.scooter.id}, "\
                F"start: {self.start_ride_time}, end: {self.end_ride_time} "

