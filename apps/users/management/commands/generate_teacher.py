from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        teacher1 = CustomUser.objects.create(
            status=CustomUser.StatusChoices.teacher,
            phone_number="+998901234567",
            password = "asd",
            email="teacher1@example.com",
            first_name="John",
            last_name="Doe",
            father_name="John",
            subject_id=1,
            mother_name="Jane",
            address="123 Main Street",
            gender=CustomUser.GenderChoices.man,
            date_of_birth="1980-01-01",
            salary=100000.00,
            bio="Experienced teacher with 5 years of experience in teaching mathematics."
        )   
        
        teacher1.groups.set([2])
        
        teacher2 = CustomUser.objects.create(
            email='teacher@example.com',
            password = "asd",
            first_name='Teacher',
            last_name='User',
            father_name="John",
            subject_id=2,
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
            password = "asd",
            first_name='Teacher3',
            last_name='User',
            father_name="John",
            subject_id=3,
            status=CustomUser.StatusChoices.teacher,
            phone_number='+998992345678',
            gender=CustomUser.GenderChoices.man,
            date_of_birth='2001-01-01',
            address='Termez',
            bio='...',
            salary=4500000
        )
        
        teacher3.groups.set([2])