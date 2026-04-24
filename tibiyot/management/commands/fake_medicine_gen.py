from django.core.management.base import BaseCommand
from faker import Faker
from tibiyot.models import Medicine

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Medicine.objects.create(
                nomi=fake.word(),
                dozasi=f"{fake.random_int(1, 3)} tablet",
                turi=fake.word(),
                muddati=f"{fake.random_int(1, 30)} kun",
                qollash_usuli=fake.text()
            )
        self.stdout.write(self.style.SUCCESS("Medicine yaratildi"))