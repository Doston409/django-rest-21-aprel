from django.core.management.base import BaseCommand
from faker import Faker
from savdo.models import Product, Category
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = list(Category.objects.all())

        for _ in range(100):
            Product.objects.create(
                nomi=fake.word(),
                kodi=fake.random_int(min=1, max=9999),
                narxi=fake.random_int(min=1000, max=100000),
                miqdori=fake.random_int(min=1, max=100),
                ishlab_chiqaruvchi=fake.company(),
                category=random.choice(categories) if categories else None
            )
        self.stdout.write(self.style.SUCCESS("Product yaratildi"))