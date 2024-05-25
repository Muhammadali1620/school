from django.contrib import admin
from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email']
    readonly_fields = ['date_joined', 'last_login']