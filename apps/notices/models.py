from django.db import models
from apps.general.models import AbstractModel
from apps.groups.services import normalize_text
from apps.exams.models import ExamResult
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field


class Notification(AbstractModel):
    class Type(models.IntegerChoices):
        EXAM_RESULT = 0, "EXAM_RESULT"
        ON_ATTENDANCE = 1, "ON_ATTENDANCE"
        STUDENT_PAYMENT = 2, "STUDENT_PAYMENT"
        SALARY = 3, "SALARY"
        ACCOUNT = 4, "ACCOUNT"
        FINE = 5, "FINE"
        WARNING = 6, "WARNING"

    notification_type = models.PositiveSmallIntegerField(choices=Type.choices)
    
    content = CKEditor5Field('content', config_name='extends')

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    exam_result = models.ForeignKey(ExamResult, on_delete=models.CASCADE, blank=True, null=True)

    is_viewed = models.BooleanField(default=False)
    viewed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_type


class Chat(AbstractModel):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               related_name='chats_sender')
    sender_email = models.CharField(max_length=255, blank=True)
    sender_phone_number = models.CharField(max_length=255, blank=True)
    sender_fullname = models.CharField(max_length=255, blank=True)
    
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                  related_name='chats_recipient')
    recipient_email = models.CharField(max_length=255, blank=True)
    recipient_phone_number = models.CharField(max_length=255, blank=True)
    recipient_fullname = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.sender_email = self.sender.email
        self.sender_phone_number = self.sender.phone_number
        self.sender_fullname = self.sender.get_full_name()
        self.recipient_email = self.recipient.email
        self.recipient_phone_number = self.recipient.phone_number
        self.recipient_fullname = self.recipient.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'recipient: {self.recipient_email}, sender: {self.sender_email}'


class Message(AbstractModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    content = models.CharField(max_length=255)
    viewed = models.BooleanField(default=False)

    viewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_short_content(self):
        return self.content[:20] + '...'

    def __str__(self):
        return self.content