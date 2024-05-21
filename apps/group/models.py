from django.db import models
from apps.users.models import CustomUser
from django.utils.timezone import now


class Subject(models.Model):
    title = models.CharField(max_length=70)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)


class Group(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                                related_name='group', related_query_name='group')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='group', related_query_name='group')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = models.Choices()

    created_at = models.DateTimeField(auto_now_add=True)


class Attendence(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                related_name='attendence', related_query_name='attendence')
    came = models.BooleanField(default=True)
    date = models.DateField(default=now())
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                              related_name='attendence', related_query_name='attendence')
    resone = models.CharField(max_length=50)