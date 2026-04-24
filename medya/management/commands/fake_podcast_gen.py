from django.core.management.base import BaseCommand
from faker import Faker
from medya.models import Podcast

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Podcast.objects.create(
                nomi=fake.word(),
                mavzusi=fake.word(),
                muallif=fake.name(),
                qismlar_soni=fake.random_int(min=1, max=200),
                platforma=fake.word()
            )
        self.stdout.write(self.style.SUCCESS("Podcast yaratildi"))