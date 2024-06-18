from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin1 = CustomUser.objects.create(
            role=CustomUser.Role.ADMIN,
            password = "asd",
            phone_number="+998909876543",
            email="admin1@example.com",
            first_name="Admin",
            last_name="Admin",
            father_name="Admin",
            mother_name="Admin",
            address="789 Oak Street",
            gender=CustomUser.Gender.MAN,
            date_of_birth="1970-01-01",
            bio="Administrator of the system.",
        )
        
        admin1.groups.set([3])

        admin2 = CustomUser.objects.create(
            email='admin@example.com',
            password = "asd",
            first_name='Admin',
            last_name='User',
            father_name="John",
            role=CustomUser.Role.ADMIN,
            phone_number='+998991234567',
            gender=CustomUser.Gender.MAN,
            date_of_birth='1980-01-01',
            address='Tashkent',
            bio='...',
        )
        
        admin2.groups.set([3])

        admin3 = CustomUser.objects.create(
            email='admin3@example.com',
            password = "asd",
            first_name='admin2',
            last_name='User',
            father_name="John",
            role=CustomUser.Role.ADMIN,
            phone_number='+998996543210',
            gender=CustomUser.Gender.WOMAN,
            date_of_birth='1985-01-01',
            address='Navoi',
            bio='...',
        )
        
        admin3.groups.set([3])

        self.stdout.write(self.style.SUCCESS(f"3-admins created"))