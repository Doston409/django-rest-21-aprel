from django.core.management.base import BaseCommand
from faker import Faker
from uy_joy.models import Apartment

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Apartment.objects.create(
                uy_raqami=fake.unique.random_int(min=1, max=500),
                xonalar_soni=fake.random_int(min=1, max=6),
                maydoni=round(fake.random_number(digits=2) + 30, 2),
                qavat=fake.random_int(min=1, max=20),
                narxi=fake.random_int(min=10000, max=500000)
            )
        self.stdout.write(self.style.SUCCESS("Apartment yaratildi"))