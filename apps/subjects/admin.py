from django.contrib import admin
from apps.subjects.models import Subject
from modeltranslation.admin import TranslationAdmin


@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    list_display = ['pk', 'slug', 'name', 'price', 'created_at']
    list_display_links = list_display
    prepopulated_fields = {'slug':['name']}
    group_fieldsets = True