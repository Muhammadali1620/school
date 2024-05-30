from django.contrib import admin
from apps.payments.models import Payment


@admin.register(Payment)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'month', 'year', 'in_percent', 'salary']
    list_display_links = list_display