from django.core.management.base import BaseCommand
from faker import Faker
from boshqa.models import Employee

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            Employee.objects.create(
                ismi=fake.first_name(),
                familiyasi=fake.last_name(),
                lavozimi=fake.job(),
                kirgan_sanasi=fake.date(),
                ish_haqi=fake.random_int(min=1000, max=5000)
            )
        self.stdout.write(self.style.SUCCESS("Employee yaratildi"))