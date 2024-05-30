from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user1 = CustomUser.objects.create(
            status=CustomUser.StatusChoices.teacher,
            phone_number="+998901234567",
            email="teacher1@example.com",
            first_name="John",
            last_name="Doe",
            father_name="John",
            mother_name="Jane",
            address="123 Main Street",
            gender=CustomUser.GenderChoices.man,
            date_of_birth="1980-01-01",
            salary=100000.00,
            bio="Experienced teacher with 5 years of experience in teaching mathematics.")

        user2 = CustomUser.objects.create(
            status=CustomUser.StatusChoices.student,
            phone_number="+998907654321",
            email="student1@example.com",
            first_name="Jane",
            last_name="Doe",
            father_name="John",
            mother_name="Jane",
            address="456 Elm Street",
            gender=CustomUser.GenderChoices.woman,
            date_of_birth="2000-01-01",
            bio="Hardworking student with a strong interest in science.")

        user3 = CustomUser.objects.create(
            status=CustomUser.StatusChoices.admin,
            phone_number="+998909876543",
            email="admin1@example.com",
            first_name="Admin",
            last_name="Admin",
            father_name="Admin",
            mother_name="Admin",
            address="789 Oak Street",
            gender=CustomUser.GenderChoices.man,
            date_of_birth="1970-01-01",
            bio="Administrator of the system.")

        self.stdout.write(self.style.SUCCESS(f"{CustomUser.objects.count()}-users created"))