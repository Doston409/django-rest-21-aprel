from django.core.management.base import BaseCommand
from faker import Faker
from savdo.models import Order, Customer
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        customers = list(Customer.objects.all())

        for _ in range(100):
            if customers:
                Order.objects.create(
                    mijoz=random.choice(customers),
                    umumiy_summa=fake.random_int(min=10000, max=500000),
                    tolov_turi=fake.word()
                )
        self.stdout.write(self.style.SUCCESS("Order yaratildi"))