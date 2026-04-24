from django.core.management.base import BaseCommand
from faker import Faker
from avtosalon.models import SparePart

fake = Faker("uz_UZ")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Fake SparePart yaratilmoqda...")

        for _ in range(100):
            SparePart.objects.create(
                nomi=fake.word(),
                qaysi_mashinaga=fake.word(),
                zavod_kodi=fake.unique.bothify(text="???-#####"),
                narxi=fake.random_int(min=100, max=5000),
                kafolati=fake.random_int(min=1, max=24)
            )

        self.stdout.write(self.style.SUCCESS("5 ta SparePart yaratildi"))