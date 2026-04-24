
from django.core.management.base import BaseCommand
from faker import Faker
from restarant.models import Waiter

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Waiter.objects.create(
                ismi=fake.first_name(),
                familiya=fake.last_name(),
                stol_raqamlari=str(fake.random_int(min=1, max=20)),
                tajribasi=fake.random_int(min=1, max=10),
                reytingi=fake.random_int(min=1, max=100)
            )
        self.stdout.write(self.style.SUCCESS("Waiter yaratildi"))