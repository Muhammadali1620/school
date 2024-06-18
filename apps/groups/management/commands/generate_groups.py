from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        can_view_subject = Permission.objects.get(codename='view_subject')
        can_view_students = Permission.objects.get(codename='view_students')
        can_view_lesson = Permission.objects.get(codename='view_lesson')
        can_view_additional_task = Permission.objects.get(codename='view_additionaltask')
        can_view_student_group = Permission.objects.get(codename='view_studentgroup')
        can_view_attendance = Permission.objects.get(codename='view_attendance')
        can_add_attendance = Permission.objects.get(codename='add_attendance')
        can_change_attendance = Permission.objects.get(codename='change_attendance')
        can_add_additional_task = Permission.objects.get(codename='add_additionaltask')
        can_change_additional_task = Permission.objects.get(codename='change_additionaltask')
        can_delete_additional_task = Permission.objects.get(codename='delete_additionaltask')


        student_group = Group.objects.create(
            name='student',
            )
        student_group.permissions.set([can_view_additional_task, can_view_lesson, can_view_subject])

        teacher_group = Group.objects.create(
            name='teacher',
            )
        teacher_group.permissions.set([can_add_additional_task, can_change_additional_task, can_delete_additional_task,
                                       can_view_additional_task, can_add_attendance, can_change_attendance,
                                       can_view_attendance, can_view_student_group,
                                       can_view_lesson, can_view_subject, can_view_students])
        
        admin_group = Group.objects.create(
            name='admin',
            )
        admin_group.permissions.set(Permission.objects.all())

        parent_group = Group.objects.create(
            name='parent',
            )
        parent_group.permissions.set([64])
        
        self.stdout.write(self.style.SUCCESS(f"{Group.objects.count()}-groups created"))