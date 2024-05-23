from django.db import models
from apps.groups.models import Subject
from apps.groups.services import normalize_text


class AdditionalTask(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='add_task', related_query_name='add_task')
    url = models.URLField()

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)