from django.core.management.base import BaseCommand
from faker import Faker
from it.models import Project

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Project.objects.create(
                nomi=fake.word(),
                muddat=fake.date(),
                byudjet=fake.random_int(min=1000, max=100000),
                masul_shaxs=fake.name(),
                holati=fake.word()
            )
        self.stdout.write(self.style.SUCCESS("Project yaratildi"))