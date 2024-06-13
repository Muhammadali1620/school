import os
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from apps.groups.services import normalize_text
from apps.users.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from apps.groups.management.commands.generate_groups import Command


@receiver(pre_save, sender=CustomUser)
def pre_save_user(instance, *args, **kwargs):
    normalize_text(instance)


@receiver(post_delete, sender=CustomUser)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    if instance.image:
        os.remove(instance.image.path)


@receiver(post_save, sender=CustomUser)
def post_save_user(instance, created, *args, **kwargs):
    if not created:
        return
    UserModel = get_user_model()
    if instance.status == UserModel.StatusChoices.student:
        instance.groups.set([1])
    if instance.status == UserModel.StatusChoices.teacher:
        instance.groups.set([2])
    if instance.status == UserModel.StatusChoices.admin:
        instance.groups.set([3])
    if instance.status == UserModel.StatusChoices.parent:
        instance.groups.set([4])