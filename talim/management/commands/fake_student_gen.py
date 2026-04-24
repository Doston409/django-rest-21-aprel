from django.core.management.base import BaseCommand
from faker import Faker
from talim.models import Student, Group
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = list(Group.objects.all())

        for _ in range(100):
            Student.objects.create(
                ism=fake.first_name(),
                familiya=fake.last_name(),
                group=random.choice(groups) if groups else None
            )
        self.stdout.write(self.style.SUCCESS("Student yaratildi"))