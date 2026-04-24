from django.core.management.base import BaseCommand
from faker import Faker
from tibiyot.models import Patient

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        for _ in range(100):
            Patient.objects.create(
                ismi=fake.first_name(),
                familiyasi=fake.last_name(),
                kasallik_tarixi=fake.text(),
                qon_guruhi=fake.random_element(blood_groups),
                yoshi=fake.random_int(min=1, max=90)
            )
        self.stdout.write(self.style.SUCCESS("Patient yaratildi"))