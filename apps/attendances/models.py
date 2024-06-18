from django.db import models
from django.conf import settings
from apps.general.models import AbstractModel
from apps.groups.models import StudentGroup
from apps.users.models import CustomUser


class Attendance(AbstractModel):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.Role.STUDENT.value},
                                related_name='student_attendance', related_query_name='student_attendance')
    came = models.BooleanField(default=True)
    date = models.DateField()
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE,
                              related_name='attendance', related_query_name='attendance')
    rezone = models.CharField(max_length=50)

    def __str__(self):
        return self.date