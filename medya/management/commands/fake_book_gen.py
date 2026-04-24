from django.core.management.base import BaseCommand
from faker import Faker
from medya.models import Book

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Book.objects.create(
                nomi=fake.word(),
                muallif=fake.name(),
                betlar_soni=fake.random_int(min=50, max=1000),
                janri=fake.word(),
                nashriyot=fake.company()
            )
        self.stdout.write(self.style.SUCCESS("Book yaratildi"))