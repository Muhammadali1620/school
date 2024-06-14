from django.db import models
from apps.general.models import AbstractModel
from apps.subjects.models import Subject
from apps.users.models import CustomUser
from django.conf import settings
from django.core.validators import MinValueValidator


class Exam(AbstractModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='exam', related_query_name='exam')
    ordering = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=255)
    limit_hour = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('ordering', 'subject')
 
    def __str__(self):
        return self.title


class ExamResult(AbstractModel):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  limit_choices_to={'status': CustomUser.StatusChoices.student.value},
                                related_name='student_exam_results', related_query_name='student_exam_results')
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True,
                             related_name='exam_results', related_query_name='exam_results')
    percent = models.PositiveSmallIntegerField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.percent 