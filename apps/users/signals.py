import os
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from apps.general.services import delete_file_after_delete_obj
from apps.users.models import CustomUser
from django.contrib.auth import get_user_model
from apps.groups.management.commands.generate_groups import Command


@receiver(post_delete, sender=CustomUser)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)


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