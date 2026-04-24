from django.core.management.base import BaseCommand
from faker import Faker
from talim.models import Group

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Group.objects.create(
                nomi=fake.word(),
                yonalishi=fake.word(),
                ochilgan_sana=fake.date(),
                talabalar_soni=fake.random_int(min=0, max=100)
            )
        self.stdout.write(self.style.SUCCESS("Group yaratildi"))