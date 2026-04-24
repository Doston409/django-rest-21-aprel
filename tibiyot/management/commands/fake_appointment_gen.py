from django.core.management.base import BaseCommand
from faker import Faker
from tibiyot.models import Appointment, Doctor, Patient
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        doctors = list(Doctor.objects.all())
        patients = list(Patient.objects.all())

        for _ in range(100):
            if doctors and patients:
                Appointment.objects.create(
                    bemor=random.choice(patients),
                    shifokor=random.choice(doctors),
                    sana=fake.date(),
                    vaqt=fake.time(),
                    shikoyati=fake.sentence()
                )
        self.stdout.write(self.style.SUCCESS("Appointment yaratildi"))