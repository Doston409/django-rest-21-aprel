
from django.core.management.base import BaseCommand
from faker import Faker
from restarant.models import Table

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Table.objects.create(
                raqami=fake.random_int(min=1, max=50),
                orinqlar_soni=fake.random_int(min=2, max=10),
                holati=fake.boolean(),
                qavat=fake.random_int(min=1, max=3)
            )
        self.stdout.write(self.style.SUCCESS("Table yaratildi"))