from django.db import models


class Car(models.Model):
    markasi = models.CharField(max_length=255)
    modeli = models.CharField(max_length=255)
    rangi = models.CharField(max_length=100)
    davlat_raqami = models.CharField(max_length=20, unique=True)
    yili = models.IntegerField()

    def __str__(self):
        return self.davlat_raqami


class Driver(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    guvohnoma_toifasi = models.CharField(max_length=10)
    tajribasi = models.IntegerField()
    reytingi = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.ismi


class Route(models.Model):
    boshlangich_nuqta = models.CharField(max_length=255)
    yakuniy_nuqta = models.CharField(max_length=255)
    masofa = models.IntegerField(default=0)
    davomiyligi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.boshlangich_nuqta} → {self.yakuniy_nuqta}"