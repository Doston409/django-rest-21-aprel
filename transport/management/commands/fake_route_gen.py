from django.core.management.base import BaseCommand
from faker import Faker
from transport.models import Route

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        cities = ["Toshkent", "Samarqand", "Buxoro", "Andijon", "Namangan"]

        for _ in range(100):
            Route.objects.create(
                boshlangich_nuqta=fake.random_element(cities),
                yakuniy_nuqta=fake.random_element(cities),
                masofa=fake.random_int(min=10, max=1000),
                davomiyligi=fake.random_int(min=1, max=20)
            )
        self.stdout.write(self.style.SUCCESS("Route yaratildi"))