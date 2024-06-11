from django.core.management import BaseCommand
from apps.additionals.models import AdditionalTask
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        task1 = AdditionalTask.objects.create(
            subject=Subject.objects.get(name="Математика"),
            title="Дополнительная задача по тригонометрии",
            slug="trig-extra-task",
            desc="Решить задачу по тригонометрии с использованием закона синусов.",
            url="https://example.com/trig-extra-task")

        task2 = AdditionalTask.objects.create(
            subject=Subject.objects.get(name="История"),
            title="Эссе по истории Древнего Рима",
            slug="ancient-rome-essay",
            desc="Написать эссе об основных событиях и достижениях Древнего Рима.",
            url="https://example.com/ancient-rome-essay")

        task3 = AdditionalTask.objects.create(
            subject=Subject.objects.get(name="Биология"),
            title="Лабораторная работа по изучению клеточного строения",
            slug="cell-structure-lab",
            desc="Провести лабораторную работу по изучению клеточного строения под микроскопом.",
            url="https://example.com/cell-structure-lab")
        
        self.stdout.write(self.style.SUCCESS(f"{AdditionalTask.objects.count()}-additional tasks created"))