from django.core.management.base import BaseCommand
from faker import Faker
from medya.models import Exhibition

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Exhibition.objects.create(
                nomi=fake.word(),
                sana=fake.date(),
                chipta_narxi=fake.random_int(min=10000, max=100000),
                mavzusi=fake.word(),
                tashkilotchi=fake.company()
            )
        self.stdout.write(self.style.SUCCESS("Exhibition yaratildi"))