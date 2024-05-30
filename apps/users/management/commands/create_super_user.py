from django.core.management import BaseCommand
from apps.users.models import CustomUser
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = input("email: ")
        password = input("password: ")
        admin = CustomUser.objects.create_superuser(status=1,
                                            phone_number='+998123456789',
                                            email=email,
                                            first_name='1',
                                            last_name='1',
                                            father_name='1',
                                            address='qattadur',
                                            gender='MAN',
                                            date_of_birth=now().date(),
                                            bio="vashshe zo'r admi",
                                            password=password)
        self.stdout.write(self.style.SUCCESS(f"Superuser added succsesfuly\nstatus: {admin.status}\nphone_number: {admin.phone_number}\nemail: {admin.email}\npassword: {password}"))