from django.core.management.base import BaseCommand
from faker import Faker
from it.models import BugReport

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100):
            BugReport.objects.create(
                loyiha_nomi=fake.word(),
                xatolik_tavsifi=fake.sentence(),
                jiddiylik_darajasi=fake.word(),
                topilgan_sana=fake.date()
            )
        self.stdout.write(self.style.SUCCESS("BugReport yaratildi"))