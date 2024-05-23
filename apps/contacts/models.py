from django.db import models
from apps.groups.models import StudentGroup
from apps.groups.services import normalize_text
from apps.users.models import CustomUser


class Notification(models.Model):
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, 
                              related_name='group_notification', related_query_name='group_notification')
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                               related_name='notification', related_query_name='notification')
    title = models.CharField(max_length=70)
    message = models.TextField(max_length=300)
    viwed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'message']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                               related_name='message', related_query_name='message')
    recipient = models.EmailField()
    title = models.CharField(max_length=70)
    desc = models.TextField(max_length=300)
    viwed = models.BooleanField(default=False)  

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)