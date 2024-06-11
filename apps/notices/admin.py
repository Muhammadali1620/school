from django.contrib import admin
from apps.notices.models import Notification, Message


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'is_viewed', 'content', 'created_at']
    list_display_links = list_display


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sender_email', 'recipient_email', 'viewed']
    list_display_links = list_display