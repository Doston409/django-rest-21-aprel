from django.core.management.base import BaseCommand
from faker import Faker
from uy_joy.models import Land

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        land_types = ["uy joy", "qishloq xo‘jaligi", "tijorat"]

        for _ in range(100):
            Land.objects.create(
                maydoni=round(fake.random_number(digits=3) / 10, 2),
                turi=fake.random_element(land_types),
                manzili=fake.address(),
                kadastr_raqami=fake.unique.bothify(text="##-####-###")
            )
        self.stdout.write(self.style.SUCCESS("Land yaratildi"))