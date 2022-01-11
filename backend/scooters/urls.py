from django.urls import path

from . import views

urlpatterns = [
    path("users/login", views.UserApiView.as_view(), name="user login"),
    path("scooters/", views.GetScootersView.as_view())
]