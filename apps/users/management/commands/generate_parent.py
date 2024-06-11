from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        parent1 = CustomUser.objects.create(
            status=CustomUser.StatusChoices.parent,
            password = "asd",
            phone_number="+998909876843",
            email="parent1@example.com",
            first_name="Parent",
            last_name="Parent",
            father_name="Parent",
            mother_name="Parent",
            address="789 Oak Street",
            gender=CustomUser.GenderChoices.man,
            child=CustomUser.objects.get(first_name='Jane'),
            date_of_birth="1970-01-01",
            bio="good Parent.")
        
        parent1.groups.set([4])

        parent2 = CustomUser.objects.create(
            email='parent2@example.com',
            password = "asd",
            first_name='Parent',
            last_name='User',
            father_name="John",
            status=CustomUser.StatusChoices.parent,
            phone_number='+998991234560',
            gender=CustomUser.GenderChoices.man,
            date_of_birth='1980-01-01',
            child=CustomUser.objects.get(first_name='Student1'),
            address='Tashkent',
            bio='...',
        )
        
        parent2.groups.set([4])

        parent3 = CustomUser.objects.create(
            email='parent3@example.com',
            password = "asd",
            first_name='parent3',
            last_name='User',
            father_name="John",
            status=CustomUser.StatusChoices.parent,
            phone_number='+998996540210',
            gender=CustomUser.GenderChoices.woman,
            date_of_birth='1985-01-01',
            child=CustomUser.objects.get(first_name='Student'),
            address='Navoi',
            bio='...',
        )
        
        parent3.groups.set([4])

        self.stdout.write(self.style.SUCCESS(f"{CustomUser.objects.count()}-users created"))