from django.db import models
from apps.groups.models import Subject
from apps.users.models import CustomUser


class Exam(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.TextField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='exam', related_query_name='exam')
    month = models.IntegerField()
    limithour = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class ExamResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  limit_choices_to={'status': CustomUser.StatusChoices.student.value},
                                related_name='student_exam_result', related_query_name='student_exam_result')
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True,
                             related_name='exam_result', related_query_name='exam_result')
    precent = models.PositiveSmallIntegerField()
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.precent