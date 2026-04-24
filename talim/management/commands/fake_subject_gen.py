from django.core.management.base import BaseCommand
from faker import Faker
from talim.models import Subject

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Subject.objects.create(
                nomi=fake.word(),
                dars_soati=fake.random_int(min=1, max=6),
                laboratoriya_borligi=fake.boolean()
            )
        self.stdout.write(self.style.SUCCESS("Subject yaratildi"))