import os
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from apps.groups.services import normalize_text
from apps.users.models import CustomUser


@receiver(pre_save, sender=CustomUser)
def pre_save_user(instance, *args, **kwargs):
    normalize_text(instance)

@receiver(post_delete, sender=CustomUser)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    if instance.image:
        os.remove(instance.image.path)