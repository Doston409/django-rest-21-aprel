from django.core.management.base import BaseCommand
from faker import Faker
from boshqa.models import HotelRoom

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            HotelRoom.objects.create(
                raqami=str(fake.random_int(min=1, max=500)),
                qavat=fake.random_int(min=1, max=10),
                turi=fake.word(),
                narxi=fake.random_int(min=100, max=1000),
                band_holati=fake.boolean()
            )
        self.stdout.write(self.style.SUCCESS("HotelRoom yaratildi"))