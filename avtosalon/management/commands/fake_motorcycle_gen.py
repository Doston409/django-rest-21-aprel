from django.core.management.base import BaseCommand
from faker import Faker
from avtosalon.models import Motorcycle

fake = Faker("uz_UZ")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Fake Motorcycle yaratilmoqda...")

        for _ in range(100):
            Motorcycle.objects.create(
                markasi=fake.company(),
                modeli=fake.word(),
                kubaturasi=fake.random_int(min=50, max=1000),
                rangi=fake.color_name(),
                narxi=fake.random_int(min=1000, max=10000)
            )

        self.stdout.write(self.style.SUCCESS("5 ta Motorcycle yaratildi"))