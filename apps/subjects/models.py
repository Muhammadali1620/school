from django.db import models
from apps.general.models import AbstractModel


class Subject(AbstractModel):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    desc = models.CharField(max_length=320)
    price = models.DecimalField(max_digits=20, decimal_places=2, help_text='Add in UZS')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name