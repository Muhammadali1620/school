from django.db import models
from apps.users.models import CustomUser
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Payment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                                limit_choices_to={'role': CustomUser.Role.STUDENT.value},
                                related_name='student_payments', related_query_name='student_payments')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                                limit_choices_to={'role': CustomUser.Role.TEACHER.value},
                                related_name='teacher_payments', related_query_name='teacher_payments', )
    month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(2020), MaxValueValidator(3000)])
    in_percent = models.PositiveSmallIntegerField()
    salary = models.DecimalField(max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (bool(self.student) + bool(self.teacher)) != 1:
            raise ValidationError('bittasini tanla')
            
    class Meta:
        unique_together = ('year', 'month', 'student', 'teacher')

    def __str__(self):
        return str(self.in_percent)