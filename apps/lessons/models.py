from django.db import models
from apps.subjects.models import Subject
from django_ckeditor_5.fields import CKEditor5Field


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ordering = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    class Meta:
        unique_together = ('ordering', 'subject')
    
    def __str__(self):
        return self.title