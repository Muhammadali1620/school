from django.db import models
from apps.general.services import normalize_txt
from django.conf import settings


class AbstractModel(models.Model):

    def save(self, *args, **kwargs):
        normalize_txt(self)
        return super().save(args, kwargs)

    class Meta:
        abstract = True