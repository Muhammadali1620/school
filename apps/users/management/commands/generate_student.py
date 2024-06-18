from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        student1 = CustomUser.objects.create(
            role=CustomUser.Role.STUDENT,
            password = "asd",
            phone_number="+998907654321",
            email="student1@example.com",
            first_name="Jane",
            last_name="Doe",
            father_name="John",
            mother_name="Jane",
            address="456 Elm Street",
            gender=CustomUser.Gender.WOMAN,
            student_group_id=1,
            date_of_birth="2000-01-01",
            bio="Hardworking student with a strong interest in science.")
        
        student1.groups.set([1])
        
        student2 = CustomUser.objects.create(
            email='student@example.com',
            password = "asd",
            first_name='Student1',
            last_name='User',
            father_name="John",
            role=CustomUser.Role.STUDENT,
            phone_number='+998993216547',
            gender=CustomUser.Gender.MAN,
            student_group_id=2,
            date_of_birth='2000-01-01',
            address='Bukhara',
            bio='...',
        )
        
        student2.groups.set([1])
        
        student3 = CustomUser.objects.create(
            email='student3@example.com',
            password = "asd",
            first_name='Student',
            last_name='User',
            father_name="John",
            role=CustomUser.Role.STUDENT,
            phone_number='+998995432101',
            gender=CustomUser.Gender.WOMAN,
            date_of_birth='1970-01-01',
            student_group_id=3,
            address='Khiva',
            bio='...',
        )
        
        student3.groups.set([1])

        self.stdout.write(self.style.SUCCESS(f"3-students created"))