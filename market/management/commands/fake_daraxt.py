from django.core.management.base import BaseCommand
from faker import Faker
from market.models import Daraxt
from random import randint
fake = Faker("uz_UZ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("fake daraxt yaratilmoqda...")
        for _ in range(10):

            Daraxt.objects.create(
                title=fake.name(),
                is_active=True if randint(0, 1) else False,
                price=randint(10000,99999),
            )
        self.stdout.write(self.style.SUCCESS("Daraxt yaratildi!"))
