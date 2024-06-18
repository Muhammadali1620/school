from django.core.management import BaseCommand
from apps.groups.models import StudentGroup
from apps.subjects.models import Subject
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        group1 = StudentGroup.objects.create(
            teacher=CustomUser.objects.get(first_name="John"),
            subject=Subject.objects.get(name="Математика"),
            start_time="10:00",
            end_time="12:00",
            week_days=[StudentGroup.WeekDays.mo, StudentGroup.WeekDays.we, StudentGroup.WeekDays.fr])

        group2 = StudentGroup.objects.create(
            teacher=CustomUser.objects.get(first_name="Teacher"),
            subject=Subject.objects.get(name="История"),
            start_time="13:00",
            end_time="15:00",
            week_days=[StudentGroup.WeekDays.tu, StudentGroup.WeekDays.th])

        group3 = StudentGroup.objects.create(
            teacher=CustomUser.objects.get(first_name="Teacher3"),
            subject=Subject.objects.get(name="Биология"),
            start_time="16:00",
            end_time="18:00",
            week_days=[StudentGroup.WeekDays.sa, StudentGroup.WeekDays.su])

        self.stdout.write(self.style.SUCCESS(f"{StudentGroup.objects.count()}-student-groups created"))