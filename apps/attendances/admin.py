from django.contrib import admin
from apps.attendances.models import Attendence


@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'student', 'came', 'date', 'resone']
    list_display_links = list_display