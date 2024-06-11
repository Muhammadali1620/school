from django.contrib import admin
from apps.additionals.models import AdditionalTask


@admin.register(AdditionalTask)
class AdditionalTaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'slug', 'url']
    list_display_links = list_display
    prepopulated_fields = {'slug':['title']}