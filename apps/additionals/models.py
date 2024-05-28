from django.db import models
from apps.subjects.models import Subject
from apps.groups.services import normalize_text
from django_ckeditor_5.fields import CKEditor5Field


class AdditionalTask(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='tasks', related_query_name='tasks')
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'desc']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)