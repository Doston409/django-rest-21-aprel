from django.core.management.base import BaseCommand
from faker import Faker
from transport.models import Driver

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = ["A", "B", "C", "D"]

        for _ in range(100):
            Driver.objects.create(
                ismi=fake.first_name(),
                familiyasi=fake.last_name(),
                guvohnoma_toifasi=fake.random_element(categories),
                tajribasi=fake.random_int(min=1, max=30),
                reytingi=round(fake.random_number(digits=2) / 10, 2)
            )
        self.stdout.write(self.style.SUCCESS("Driver yaratildi"))