from django.core.management.base import BaseCommand
from faker import Faker
from avtosalon.models import AutoService

fake = Faker("uz_UZ")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Fake AutoService yaratilmoqda...")

        for _ in range(100):
            AutoService.objects.create(
                klient_ismi=fake.first_name(),
                mashina_raqami=fake.bothify(text="##-???-##"),
                muammo=fake.sentence(),
                usta_ismi=fake.name(),
                narxi=fake.random_int(min=50000, max=2000000)
            )

        self.stdout.write(self.style.SUCCESS("5 ta AutoService yaratildi"))