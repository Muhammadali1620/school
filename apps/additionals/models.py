from django.db import models
from apps.general.models import AbstractModel
from apps.subjects.models import Subject


class AdditionalTask(AbstractModel):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='tasks', related_query_name='tasks')
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title