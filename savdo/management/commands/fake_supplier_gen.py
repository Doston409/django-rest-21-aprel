from django.core.management.base import BaseCommand
from faker import Faker
from savdo.models import Supplier

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Supplier.objects.create(
                kompaniya_nomi=fake.company(),
                masul_shaxs=fake.name(),
                telefon=fake.phone_number(),
                yetkazish_muddati=fake.word()
            )
        self.stdout.write(self.style.SUCCESS("Supplier yaratildi"))