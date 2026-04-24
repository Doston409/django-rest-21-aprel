from django.core.management.base import BaseCommand
from faker import Faker
from fintech.models import Teacher
fake = Faker("uz_UZ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("fake studentlar yaratilmoqda...")
        print(fake.name())
        print(fake.address())
        for _ in range(10):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                specialization="Dasturchi",
                
            )
        self.stdout.write(self.style.SUCCESS("Student yaratildi"))