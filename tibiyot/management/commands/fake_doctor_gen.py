from django.core.management.base import BaseCommand
from faker import Faker
from tibiyot.models import Doctor

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):

        fake.unique.clear()

        for _ in range(100):
            Doctor.objects.create(
                ismi=fake.first_name(),
                familiyasi=fake.last_name(),
                mutaxassisligi=fake.word(),
                xona_raqami=fake.unique.random_int(min=1, max=1000),
                tajribasi=fake.random_int(min=1, max=30)
            )

        self.stdout.write(self.style.SUCCESS("Doctor yaratildi"))