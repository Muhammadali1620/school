from django.core.management import BaseCommand
from apps.exams.models import Exam
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        exam1 = Exam.objects.create(
            subject=Subject.objects.get(name="Математика"),
            ordering=1,
            title="Экзамен по тригонометрии",
            slug="trig-exam",
            desc="Экзамен по основным понятиям тригонометрии, тригонометрическим функциям и их свойствам.",
            limit_hour=2)

        exam2 = Exam.objects.create(
            subject=Subject.objects.get(name="История"),
            ordering=2,
            title="Экзамен по истории Древнего мира",
            slug="ancient-world-history-exam",
            desc="Экзамен по основным событиям и достижениям истории Древнего мира, включая Древний Египет, Месопотамию и Древнюю Грецию.",
            limit_hour=3)

        exam3 = Exam.objects.create(
            subject=Subject.objects.get(name="Биология"),
            ordering=3,
            title="Экзамен по общей биологии",
            slug="general-biology-exam",
            desc="Экзамен по основным понятиям биологии, включая строение и функции клетки, генетику и эволюцию.",
            limit_hour=2)
        
        self.stdout.write(self.style.SUCCESS(f"{Exam.objects.count()}-exams created"))