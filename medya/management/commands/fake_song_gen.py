from django.core.management.base import BaseCommand
from faker import Faker
from medya.models import Song

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Song.objects.create(
                nomi=fake.word(),
                ijrochi=fake.name(),
                janri=fake.word(),
                davomiyligi=fake.random_int(min=120, max=400),
                yili=fake.random_int(min=1990, max=2025)
            )
        self.stdout.write(self.style.SUCCESS("Song yaratildi"))