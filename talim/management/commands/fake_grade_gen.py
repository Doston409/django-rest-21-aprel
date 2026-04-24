from django.core.management.base import BaseCommand
from faker import Faker
from talim.models import Grade, Student, Subject
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        students = list(Student.objects.all())
        subjects = list(Subject.objects.all())

        for _ in range(100):
            if students and subjects:
                Grade.objects.create(
                    student=random.choice(students),
                    fan=random.choice(subjects),
                    baho=fake.random_int(min=1, max=5),
                    sana=fake.date()
                )
        self.stdout.write(self.style.SUCCESS("Grade yaratildi"))