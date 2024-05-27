from django.contrib import admin
from apps.tasks.models import Lesson


@admin.register(Lesson)
class LessonUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'ordering']
    list_display_links = list_display