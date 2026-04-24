from django.core.management.base import BaseCommand
from faker import Faker
from boshqa.models import Movie

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Movie.objects.create(
                nomi=fake.word(),
                janri=fake.word(),
                rejissyor=fake.name(),
                davomiyligi=fake.random_int(min=60, max=180),
                chiqish_yili=fake.random_int(min=1990, max=2025)
            )
        self.stdout.write(self.style.SUCCESS("Movie yaratildi"))