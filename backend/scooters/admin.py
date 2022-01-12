from django.contrib import admin

# Register your models here.
from .models import Provider, Scooter, User

admin.site.register(Provider)
admin.site.register(Scooter)
admin.site.register(User)
