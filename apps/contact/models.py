from email.headerregistry import Group
from django.db import models
from apps.users.models import CustomUser


class Notification(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, 
                              related_name='notification', related_query_name='notification')
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                               related_name='notification', related_query_name='notification')
    title = models.CharField(max_length=70)
    message = models.TextField(max_length=300)
    viwed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                               related_name='notification', related_query_name='notification')
    recipient = models.EmailField()
    title = models.CharField(max_length=70)
    desc = models.TextField(max_length=300)
    viwed = models.BooleanField(default=False)  

    def __str__(self):
        return self.title