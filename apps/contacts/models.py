from django.db import models
from apps.groups.services import normalize_text
from apps.tasks.models import ExamResult
from apps.users.models import CustomUser


class Notification(models.Model):
    class Type(models.IntegerChoices):
        EXAM_RESULT = 0, "EXAM_RESULT"
        ON_ATTENDANCE = 1, "ON_ATTENDANCE"
        STUDENT_PAYMENT = 2, "STUDENT_PAYMENT"
        SELARY = 3, "SELARY"
        ACCOUNT = 4, "ACCOUNT"
        FINE = 5, "FINE"
        WARNING = 6, "WARNING"

    notification_type = models.PositiveSmallIntegerField(choices=Type.choices)
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)

    student = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, blank=True, null=True)
    exam_result = models.ForeignKey(ExamResult, on_delete=models.CASCADE, blank=True, null=True)

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
                               related_name='messages_sender', related_query_name='messages_sender')
    sender_email = models.CharField()
    sender_phone_number = models.CharField()
    sender_fullname = models.CharField()
    recipient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                                  related_name='messages_recipient', related_query_name='messages_recipient')
    recipient_email = models.CharField
    recipient_phone_number = models.CharField()
    recipient_fullname = models.CharField()

    title = models.CharField(max_length=70)
    desc = models.CharField(max_length=255)
    viwed = models.BooleanField(default=False)  

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)