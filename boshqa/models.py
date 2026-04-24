from django.db import models


class HotelRoom(models.Model):
    raqami = models.CharField(max_length=20)
    qavat = models.IntegerField(default=0)
    turi = models.CharField(max_length=50)
    narxi = models.IntegerField(default=0)
    band_holati = models.BooleanField(default=False)

    def __str__(self):
        return f"Xona {self.raqami}"


class Employee(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
    kirgan_sanasi = models.DateField()
    ish_haqi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ismi} {self.familiyasi}"


class Movie(models.Model):
    nomi = models.CharField(max_length=255)
    janri = models.CharField(max_length=255)
    rejissyor = models.CharField(max_length=255)
    davomiyligi = models.IntegerField(default=0)
    chiqish_yili = models.IntegerField(default=0)

    def __str__(self):
        return self.nomi