from django.core.management.base import BaseCommand
from faker import Faker
from sport.models import Gym

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Gym.objects.create(
                nomi=fake.company(),
                manzili=fake.address(),
                oylik_abonement_narxi=fake.random_int(min=100000, max=1000000),
                ish_vaqti="08:00 - 22:00"
            )
        self.stdout.write(self.style.SUCCESS("Gym yaratildi"))