from django.db import models
from apps.group.models import Subject
from apps.users.models import CustomUser


class Exam(models.Model):
    title = models.CharField(max_length=70)
    desc = models.TextField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='exam', related_query_name='exam')
    month = models.IntegerField()
    limithour = models.TimeField()


class ExamResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                related_name='exam_result', related_query_name='exam_result')
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True,
                             related_name='exam_result', related_query_name='exam_result')
    precent = models.PositiveIntegerField()
    comment = models.TextField(max_length=300)