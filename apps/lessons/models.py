from django.db import models
from apps.general.models import AbstractModel
from apps.subjects.models import Subject


class Lesson(AbstractModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ordering = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    class Meta:
        unique_together = ('ordering', 'subject')
    
    def __str__(self):
        return self.title