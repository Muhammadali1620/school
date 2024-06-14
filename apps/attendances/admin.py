from django.contrib import admin
from apps.attendances.models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'student', 'came', 'date', 'rezone']
    list_display_links = list_display