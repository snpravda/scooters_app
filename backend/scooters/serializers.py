from rest_framework import serializers

from .models import User, Scooter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        email = serializers.CharField()
        fields = ("email",)


class GetScootersSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source="provider.name")
    price_per_hour = serializers.CharField(source="provider.price_per_hour")

    class Meta:
        model = Scooter
        fields = ("id", "latitude", "longitude", "battery_percentage", "price_per_hour", "provider_name",)


class StartStopRideSerializer(serializers.Serializer):
    email = serializers.EmailField()
