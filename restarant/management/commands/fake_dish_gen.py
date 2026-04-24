from django.core.management.base import BaseCommand
from faker import Faker
from restarant.models import Dish

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Dish.objects.create(
                nomi=fake.word(),
                tarkibi=fake.text(),
                narxi=fake.random_int(min=10000, max=100000),
                kaloriyasi=fake.random_int(min=100, max=1000),
                tayyorlanish_vaqti=fake.random_int(min=5, max=60)
            )
        self.stdout.write(self.style.SUCCESS("Dish yaratildi"))