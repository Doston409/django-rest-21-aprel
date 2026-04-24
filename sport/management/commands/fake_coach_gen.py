from django.core.management.base import BaseCommand
from faker import Faker
from sport.models import Coach

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Coach.objects.create(
                ismi=fake.first_name(),
                familiya=fake.last_name(),
                tajribasi=fake.random_int(min=1, max=20),
                ixtisosligi=fake.word(),
                oylik_maosh=fake.random_number(digits=6)
            )
        self.stdout.write(self.style.SUCCESS("Coach yaratildi"))