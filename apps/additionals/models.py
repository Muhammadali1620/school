from django.db import models
from apps.groups.models import Subject
from apps.groups.services import normalize_text


class AdditionalTask(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='tasks', related_query_name='tasks')
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=500)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)