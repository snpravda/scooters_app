from django.db.models import Q
from django.http import HttpResponse
from rest_framework import parsers, renderers, status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer, GetScootersSerializer


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
