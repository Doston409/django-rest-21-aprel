from django.core.management.base import BaseCommand
from faker import Faker
from sport.models import Competition

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Competition.objects.create(
                nomi=fake.word(),
                sana=fake.date(),
                mukofot_jamgarmasi=fake.random_int(min=1000000, max=100000000),
                manzili=fake.address()
            )
        self.stdout.write(self.style.SUCCESS("Competition yaratildi"))