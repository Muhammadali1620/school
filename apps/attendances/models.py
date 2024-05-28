from django.db import models
from django.conf import settings
from apps.groups.models import StudentGroup
from apps.groups.services import normalize_text
from apps.users.models import CustomUser


class Attendence(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'status': CustomUser.StatusChoices.student.value},
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