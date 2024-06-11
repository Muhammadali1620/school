from django.core.management import BaseCommand
from apps.payments.models import Payment
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment1 = Payment.objects.create(
            student=CustomUser.objects.get(first_name="Jane"),
            month=9,
            year=2023,
            in_percent=100,
            salary=100000.00
        )

        payment2 = Payment.objects.create(
            teacher=CustomUser.objects.get(first_name="John"),
            month=10,
            year=2023,
            in_percent=100,
            salary=50000.00
        )

        payment3 = Payment.objects.create(
            teacher=CustomUser.objects.get(first_name="John"),
            month=11,
            year=2023,
            in_percent=100,
            salary=150000.00
        )
        
        self.stdout.write(self.style.SUCCESS(f"{Payment.objects.count()}-payments created"))