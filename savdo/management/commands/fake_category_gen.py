from django.core.management.base import BaseCommand
from faker import Faker
from savdo.models import Category

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Category.objects.create(
                nomi=fake.word(),
                tavsifi=fake.text(),
                rasm_url=fake.image_url()
            )
        self.stdout.write(self.style.SUCCESS("Category yaratildi"))