from django.contrib import admin
from apps.groups.models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'slug', 'name', 'price', 'created_at']
    list_display_links = list_display
    prepopulated_fields = {'slug':['name']}