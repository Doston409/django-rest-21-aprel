from django.core.management.base import BaseCommand
from faker import Faker
from transport.models import Car

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        colors = ["qizil", "qora", "oq", "ko‘k", "kulrang"]

        for _ in range(100):
            Car.objects.create(
                markasi=fake.company(),
                modeli=fake.word(),
                rangi=fake.random_element(colors),
                davlat_raqami=fake.unique.bothify(text="##-???-##"),
                yili=fake.random_int(min=1995, max=2025)
            )
        self.stdout.write(self.style.SUCCESS("Car yaratildi"))