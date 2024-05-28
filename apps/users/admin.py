from django.contrib import admin
from django.conf import settings
from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'phone_number', 'get_full_name', 'gender', 'date_of_birth']
    list_display_links = list_display
    readonly_fields = ['date_joined', 'last_login']