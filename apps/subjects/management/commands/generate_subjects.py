from django.core.management import BaseCommand
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        subject1 = Subject.objects.create(
            name="Математика",
            slug="math",
            desc="Раздел науки, занимающийся изучением отношений величин, свойств фигур, изменений состояний объектов и процессов, происходящих в окружающем мире.",
            price=100000.00)
        
        subject2 = Subject.objects.create(
            name="История",
            slug="history",
            desc="Наука, изучающая прошлое человеческого общества по письменным и вещественным источникам.",
            price=120000.00)
        
        subject3 = Subject.objects.create(
            name="Биология",
            slug="biology",
            desc="Наука о живых организмах, их строении, жизнедеятельности, происхождении и развитии.",
            price=150000.00)

        self.stdout.write(self.style.SUCCESS(f"{Subject.objects.count()}-subjects created"))
