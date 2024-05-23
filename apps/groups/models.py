from django.db import models
from apps.groups.services import normalize_text
from apps.users.models import CustomUser
from django.utils.timezone import now


class Subject(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['name', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)



class StudentGroup(models.Model):

    class Weekdays(models.IntegerChoices):
        su = 0, 'Sunday'
        mo = 1, 'Monday'
        tu = 2, 'Tuesday'
        we = 3, 'Wednesday'
        th = 4, 'Thursday'
        fr = 5, 'Friday'
        sa = 6, 'Saturday'

    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, limit_choices_to={'status': CustomUser.StatusChoices.teacher.value},
                                related_name='group', related_query_name='group')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='group', related_query_name='group')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = models.PositiveSmallIntegerField(choices=Weekdays.choices)

    created_at = models.DateTimeField(auto_now_add=True)

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