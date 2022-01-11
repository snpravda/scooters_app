from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/login', views.UserApiView.as_view(), name="user login"),
]