from django.core.management.base import BaseCommand
from faker import Faker
from savdo.models import Customer

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Customer.objects.create(
                ism=fake.first_name(),
                familiya=fake.last_name(),
                telefon=fake.phone_number(),
                manzili=fake.address(),
                jami_xaridi=fake.random_int(min=0, max=1000000)
            )
        self.stdout.write(self.style.SUCCESS("Customer yaratildi"))