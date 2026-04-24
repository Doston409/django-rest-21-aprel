from django.core.management.base import BaseCommand
from faker import Faker
from uy_joy.models import Building

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        types = ["uy", "biznes markaz", "mehmonxona"]

        for _ in range(100):
            Building.objects.create(
                nomi=fake.company(),
                qavatlar_soni=fake.random_int(min=1, max=30),
                qurilgan_yili=fake.random_int(min=1980, max=2025),
                manzili=fake.address(),
                turi=fake.random_element(types)
            )
        self.stdout.write(self.style.SUCCESS("Building yaratildi"))