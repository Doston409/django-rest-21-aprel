from django.core.management.base import BaseCommand
from faker import Faker
from market.models import Category
from random import randint
fake = Faker("uz_UZ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("fake Categorlar yaratilmoqda...")
        for _ in range(10):

            Category.objects.create(
                name=fake.name(),
                is_active=True if randint(0, 1) else False
            )
        self.stdout.write(self.style.SUCCESS("Categorlar yaratildi!"))
