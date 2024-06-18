from django.core.management import BaseCommand
from apps.users.models import CustomUser
from django.utils.timezone import now
from django.contrib.auth.base_user import BaseUserManager


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = input("email: ")
        password = input("password: ")
        norm_email = BaseUserManager.normalize_email(email)
        admin = CustomUser.objects.create_superuser(role=1,
                                            phone_number='+998123456789',
                                            email=norm_email,
                                            first_name='1',
                                            last_name='1',
                                            father_name='1',
                                            address='qattadur',
                                            gender='MAN',
                                            date_of_birth=now().date(),
                                            bio="vashshe zo'r admi",
                                            password=password)
        self.stdout.write(self.style.SUCCESS(f"Superuser added successfully\nrole: {admin.role}\nphone_number: {admin.phone_number}\nemail: {admin.email}\npassword: {password}"))