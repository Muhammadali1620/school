from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        teacher1 = CustomUser.objects.create(
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
        
        teacher1.groups.set([2])
        
        teacher2 = CustomUser.objects.create(
            email='teacher@example.com',
            first_name='Teacher',
            last_name='User',
            status=CustomUser.StatusChoices.teacher,
            phone_number='+998997654321',
            gender=CustomUser.GenderChoices.woman,
            date_of_birth='1990-01-01',
            address='Samarkand',
            bio='...',
            salary=5000000,
        )
        
        teacher2.groups.set([2])

        teacher3 = CustomUser.objects.create(
            email='teacher3@example.com',
            first_name='Teacher3',
            last_name='User',
            status=CustomUser.StatusChoices.teacher,
            phone_number='+998992345678',
            gender=CustomUser.GenderChoices.man,
            date_of_birth='2001-01-01',
            address='Termez',
            bio='...',
            salary=4500000
        )
        
        teacher3.groups.set([2])

        student1 = CustomUser.objects.create(
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
        
        student1.groups.set([1])
        
        student2 = CustomUser.objects.create(
            email='student@example.com',
            first_name='Student',
            last_name='User',
            status=CustomUser.StatusChoices.student,
            phone_number='+998993216547',
            gender=CustomUser.GenderChoices.man,
            date_of_birth='2000-01-01',
            address='Bukhara',
            bio='...',
                )
        
        student2.groups.set([1])
        
        student3 = CustomUser.objects.create(
            email='student3@example.com',
            first_name='Student',
            last_name='User',
            status=CustomUser.StatusChoices.student,
            phone_number='+998995432101',
            gender=CustomUser.GenderChoices.woman,
            date_of_birth='1970-01-01',
            address='Khiva',
            bio='...',
        )
        
        student3.groups.set([1])

        admin1 = CustomUser.objects.create(
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
        
        admin1.groups.set([3])

        admin2 = CustomUser.objects.create(
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            status=CustomUser.StatusChoices.admin,
            phone_number='+998991234567',
            gender=CustomUser.GenderChoices.man,
            date_of_birth='1980-01-01',
            address='Tashkent',
            bio='...',
            salary=0,
        )
        
        admin2.groups.set([3])

        admin3 = CustomUser.objects.create(
            email='admin3@example.com',
            first_name='admin2',
            last_name='User',
            status=CustomUser.StatusChoices.admin,
            phone_number='+998996543210',
            gender=CustomUser.GenderChoices.woman,
            date_of_birth='1985-01-01',
            address='Navoi',
            bio='...',
        )
        
        admin1.groups.set([3])

        self.stdout.write(self.style.SUCCESS(f"{CustomUser.objects.count()}-users created"))