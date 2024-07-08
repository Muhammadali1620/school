from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models

from apps.general.models import AbstractModel
from apps.subjects.models import Subject
from apps.users.models import CustomUser


class StudentGroup(AbstractModel):
    class Weekdays(models.IntegerChoices):
        Mo = 0, 'monday'
        Tu = 1, 'tuesday'
        We = 2, 'wednesday'
        Th = 3, 'thursday'
        Fr = 4, 'friday'
        Sa = 5, 'saturday'
        Su = 6, 'sunday'

    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='subject_groups')
    teacher = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.Teacher.value},
                                on_delete=models.PROTECT, related_name='teacher_groups')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = ArrayField(base_field=models.PositiveSmallIntegerField(choices=Weekdays.choices))
    create_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.start_time.strftime("%H:%M")}~{self.end_time.strftime("%H:%M")}'

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError({'end_time': 'time not valid.'})

        if StudentGroup.objects.filter(teacher_id=self.teacher.pk, week_days=self.week_days).filter(
                models.Q(start_time__range=(self.start_time, self.end_time))
                |
                models.Q(end_time__range=(self.start_time, self.end_time))
        ).exists():
            raise ValidationError(f'{self.teacher}ning {self.start_time}-{self.end_time} oralig\'ida darsi bor')
