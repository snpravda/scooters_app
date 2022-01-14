from django.contrib import admin

# Register your models here.
from .models import Provider, Scooter, User, Ride


class HistoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Provider)
admin.site.register(Scooter)
admin.site.register(User)
admin.site.register(Ride, HistoryAdmin)
