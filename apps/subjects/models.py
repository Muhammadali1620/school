from django.db import models
from apps.groups.services import normalize_text


class Subject(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    desc = models.CharField(max_length=255)
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