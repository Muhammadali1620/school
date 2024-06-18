from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        student1 = CustomUser.objects.get(first_name='Jane')
        student2 = CustomUser.objects.get(first_name='Student1')
        student3 = CustomUser.objects.get(first_name='Student')

        parent1 = CustomUser.objects.create(
            role=CustomUser.Role.PARENT,
            password = "asd",
            phone_number="+998909876843",
            email="parent1@example.com",
            first_name="Parent",
            last_name="Parent",
            father_name="Parent",
            mother_name="Parent",
            address="789 Oak Street",
            gender=CustomUser.Gender.MAN,
            date_of_birth="1970-01-01",
            bio="good Parent.")
        
        parent1.groups.set([4])
        parent1.children.set([student1.id])

        parent2 = CustomUser.objects.create(
            email='parent2@example.com',
            password = "asd",
            first_name='Parent',
            last_name='User',
            father_name="John",
            role=CustomUser.Role.PARENT,
            phone_number='+998991234560',
            gender=CustomUser.Gender.MAN,
            date_of_birth='1980-01-01',
            address='Tashkent',
            bio='...',
        )
        
        parent2.groups.set([4])
        parent2.children.set([student2.id])

        parent3 = CustomUser.objects.create(
            email='parent3@example.com',
            password = "asd",
            first_name='parent3',
            last_name='User',
            father_name="John",
            role=CustomUser.Role.PARENT,
            phone_number='+998996540210',
            gender=CustomUser.Gender.WOMAN,
            date_of_birth='1985-01-01',
            address='Navoi',
            bio='...',
        )
        
        parent3.groups.set([4])
        parent3.children.set([student3.id])

        self.stdout.write(self.style.SUCCESS(f"3-parents created"))