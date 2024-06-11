from django.contrib import admin
from django.conf import settings
from apps.users.models import CustomUser
from django.contrib.auth.models import Permission


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status', 'email', 'phone_number', 'get_full_name', 'gender', 'date_of_birth']
    list_display_links = list_display
    readonly_fields = ['date_joined', 'last_login']
    fields = [('first_name', 'last_name'), 'password', 'email', 'phone_number', 'status', 'date_of_birth', 'groups',
              'subject', 'user_permissions', 'student_group', 'is_active', 'is_staff', 'last_login',
              'father_name', 'mother_name', 'address', 'gender', 'bio', 'child', 'salary',
              'image', 'date_joined', 'zip_code']
    
    def save_model(self, request, obj, form, change):
        if obj.password != form.initial.get('password'):
            obj.set_password(obj.password)
        obj.save()


# @admin.register(Permission)
# class PermissionAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'codename']
#     list_display_links = list_display
#     search_fields = ['name', 'codename']
#     ordering = ['id']