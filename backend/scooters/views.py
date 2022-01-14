from rest_framework import parsers, renderers, status
from rest_framework.generics import GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response

from .models import *
from .serializers import *


class UserApiView(GenericAPIView):
    """Is Used for creating user by email if user does not exists. If user exists nothing will happen"""
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            email = request.data["email"]
            if User.objects.filter(email=email):
                msg = f"user with email {email} already exists"
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                msg = f"user with email {email} successfully created"

            return Response({"result": msg}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"result": "ERROR " + str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetScootersView(ListAPIView):
    """Returns all free scooters"""
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = GetScootersSerializer

    def get_queryset(self):
        return Scooter.objects.filter(used_by_user=None)


class ScootersStartRideView(GenericAPIView):
    """Starts ride on scooter, if scooter is already on ride nothing will happen"""
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = StartStopRideSerializer

    def post(self, request, scooter_id):
        try:
            scooter: Scooter = get_object_or_404(Scooter, pk=scooter_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if scooter.used_by_user:
                return  Response(
                    {"success": False, "error": f"Ride already started at {scooter.last_ride.start_ride_time}"},
                    status=status.HTTP_200_OK)

            user: User = get_object_or_404(User, email=serializer.data["email"])

            new_ride = Ride(user=user, scooter=scooter)
            new_ride.save()

            scooter.used_by_user = user
            scooter.last_ride = new_ride
            scooter.save()

            return Response(
                {"success": True, "result": f"new ride started at {new_ride.start_ride_time}"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"success": False, "error": "ERROR " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
