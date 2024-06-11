from django.contrib import admin
from apps.lessons.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'ordering']
    list_display_links = list_display