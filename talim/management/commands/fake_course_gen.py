from django.core.management.base import BaseCommand
from faker import Faker
from talim.models import Course

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Course.objects.create(
                nomi=fake.word(),
                narxi=fake.random_number(digits=5),
                davomiyligi=fake.random_int(min=1, max=12),
                darajasi=fake.word()
            )
        self.stdout.write(self.style.SUCCESS("Course yaratildi"))