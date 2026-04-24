from django.core.management.base import BaseCommand
from faker import Faker
from it.models import Laptop

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Laptop.objects.create(
                brend=fake.company(),
                protsessor=fake.word(),
                ram_hajmi=fake.random_int(min=4, max=64),
                xotira=f"{fake.random_int(min=128, max=2000)} GB",
                narxi=fake.random_int(min=300, max=3000)
            )
        self.stdout.write(self.style.SUCCESS("Laptop yaratildi"))