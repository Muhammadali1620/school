from django.db import models
from apps.groups.services import normalize_text
from apps.users.models import CustomUser
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field


class Subject(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    desc = CKEditor5Field('Text', config_name='extends')
    price = models.DecimalField(max_digits=20, decimal_places=2, help_text='Add in UZS')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_normalize_fields(cls):
        return ['name', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)



class StudentGroup(models.Model):

    class Weekdays(models.IntegerChoices):
        mo = 0, 'Monday'
        tu = 1, 'Tuesday'
        we = 2, 'Wednesday'
        th = 3, 'Thursday'
        fr = 4, 'Friday'
        sa = 5, 'Saturday'
        su = 6, 'Sunday'

    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, limit_choices_to={'status': CustomUser.StatusChoices.teacher.value},
                                related_name='teacher_groups', related_query_name='teacher_groups')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='student_groups', related_query_name='student_groups')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = models.PositiveSmallIntegerField(choices=Weekdays.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValueError({'end_time': 'End time must greater than start time.'})
        if StudentGroup.objects.filter(teacher_id=self.teacher.pk, week_days=self.week_days).filter(
            models.Q(start_time__range=(self.start_time, self.end_time))
            |
            models.Q(end_time__range=(self.start_time, self.end_time))
        ).exists():
            raise ValidationError(f"{self.teacher} o'qituvchining [{self.start_time}~{self.end_time}] vaqt oralig'ida darsi bor")

    def __str__(self):
        return self.week_days
    

class Attendence(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'status': CustomUser.StatusChoices.student.value},
                                related_name='student_attendence', related_query_name='student_attendence')
    came = models.BooleanField(default=True)
    date = models.DateField()
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE,
                              related_name='attendence', related_query_name='attendence')
    resone = models.CharField(max_length=50)

    def __str__(self):
        return self.date
    
    @classmethod
    def get_normalize_fields(cls):
        return ['resone']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)