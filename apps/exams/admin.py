from django.contrib import admin
from apps.exams.models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'ordering', 'title', 'limit_hour']
    list_display_links = list_display