from django.db import models
from apps.users.models import CustomUser
from django.core.exceptions import ValidationError


class Payment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'status': CustomUser.StatusChoices.student.value},
                                related_name='student_payment', related_query_name='student_payment')
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'status': CustomUser.StatusChoices.teacher.value},
                                related_name='teacher_payment', related_query_name='teacher_payment', )
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    in_percent = models.BooleanField(default=False)
    slelery = models.DecimalField(max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (bool(self.student) + bool(self.student)) != 1:
            raise ValidationError('bittasini tanla')
            
    class Meta:
        unique_together = ('year', 'month', 'student', 'teacher')

    def __str__(self):
        return self.in_percent