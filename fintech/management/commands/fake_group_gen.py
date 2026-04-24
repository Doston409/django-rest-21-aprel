from django.core.management.base import BaseCommand
from faker import Faker
from fintech.models import Group, Teacher
fake = Faker("uz_UZ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("fake Group yaratilmoqda...")
        print(fake.name())
        print(fake.address())
        for _ in range(10):
            teacher = Teacher.objects.all().order_by("?").first()
            Group.objects.create(
                name=fake.name(),
                teacher=teacher,
                
                
            )
        self.stdout.write(self.style.SUCCESS("Group yaratildi"))