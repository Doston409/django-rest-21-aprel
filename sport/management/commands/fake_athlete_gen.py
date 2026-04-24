from django.core.management.base import BaseCommand
from faker import Faker
from sport.models import Athlete

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Athlete.objects.create(
                ismi=fake.first_name(),
                familiya=fake.last_name(),
                sport_turi=fake.word(),
                boyi=round(fake.random_number(digits=3) / 100, 2),
                vazni=round(fake.random_number(digits=2) + 40, 2)
            )
        self.stdout.write(self.style.SUCCESS("Athlete yaratildi"))
