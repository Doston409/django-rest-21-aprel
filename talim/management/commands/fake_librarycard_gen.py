from django.core.management.base import BaseCommand
from faker import Faker
from talim.models import LibraryCard, Student

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        students = list(Student.objects.all())

        for _ in range(100):
            if students:
                LibraryCard.objects.create(
                    student=fake.random_element(students),
                    berilgan_sana=fake.date(),
                    amal_qilish_muddati=fake.date()
                )
        self.stdout.write(self.style.SUCCESS("LibraryCard yaratildi"))