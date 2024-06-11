from django.core.management import BaseCommand
from apps.lessons.models import Lesson
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        lesson1 = Lesson.objects.create(
            subject=Subject.objects.get(name="Математика"),
            ordering=1,
            title="Введение в тригонометрию",
            desc="Основные понятия тригонометрии, углы, стороны треугольника, тригонометрические функции.")

        lesson2 = Lesson.objects.create(
            subject=Subject.objects.get(name="История"),
            ordering=2,
            title="Древний Египет",
            desc="Возникновение и развитие древнеегипетской цивилизации, ее основные достижения и наследие.")

        lesson3 = Lesson.objects.create(
            subject=Subject.objects.get(name="Биология"),
            ordering=3,
            title="Клетка как структурно-функциональная единица живого",
            desc="Строение и функции основных компонентов клетки, процессы жизнедеятельности клетки.")
        
        self.stdout.write(self.style.SUCCESS(f"{Lesson.objects.count()}-lessons created"))