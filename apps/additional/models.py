from django.db import models
from apps.group.models import Subject


class AdittionalTask(models.Model):
    title = models.CharField(max_length=70)
    desc = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='add_task', related_query_name='add_task')
    url = models.URLField()