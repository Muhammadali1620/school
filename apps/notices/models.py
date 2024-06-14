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


class Message(AbstractModel):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               related_name='messages_sender', related_query_name='messages_sender')
    sender_email = models.CharField(max_length=255)
    sender_phone_number = models.CharField(max_length=255)
    sender_fullname = models.CharField(max_length=255)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                  related_name='messages_recipient', related_query_name='messages_recipient')
    recipient_email = models.CharField(max_length=255)
    recipient_phone_number = models.CharField(max_length=255)
    recipient_fullname = models.CharField(max_length=255)

    content = models.CharField(max_length=255)
    viewed = models.BooleanField(default=False)

    viewed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title