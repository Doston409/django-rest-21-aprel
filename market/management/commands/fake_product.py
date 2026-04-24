from django.core.management.base import BaseCommand
from faker import Faker
from market.models import Product, Category
from random import randint
fake = Faker("uz_UZ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("fake Productlar yaratilmoqda...")
        categories = Category.objects.all()
        for _ in range(100):
            cateogry = categories.order_by("?").first()
            Product.objects.create(
                category=cateogry,
                name=fake.name(),
                price=randint(10000,99999),
                is_active=True if randint(0, 1) else False
            )
        self.stdout.write(self.style.SUCCESS("Productlar yaratildi!"))
