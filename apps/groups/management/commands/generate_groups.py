from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_group = Group.objects.create(
            name='student',
            )
        student_group.permissions.set([24, 52, 64])

        teacher_group = Group.objects.create(
            name='teacher',
            )
        teacher_group.permissions.set([21, 22, 23, 24, 25, 26, 28, 44, 48, 52, 64])
        
        admin_group = Group.objects.create(
            name='admin',
            )
        admin_group.permissions.set(Permission.objects.all())
        
        self.stdout.write(self.style.SUCCESS(f"{Group.objects.count()}-groups created"))