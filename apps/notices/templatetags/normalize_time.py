import datetime
from django import template
from django.utils.timezone import now, timedelta


register = template.Library()

@register.filter
def datetime_to_minute(created_at):
    if type(created_at) != datetime.datetime:
        return 'No messages yet'
    current_datetime = now() - created_at
    seconds = current_datetime.total_seconds()
    if seconds < 60:
        return f"{int(seconds)} seconds ago"

    minutes = seconds // 60
    if minutes < 60:
        return f"{int(minutes)} minutes ago"

    hours = minutes // 60
    if hours < 24:
        return f"{int(hours)} hours ago"

    days = hours // 24
    if days < 7:
        return f"{int(days)} days ago"

    weeks = days // 7

    return f"{int(weeks)} weeks ago"