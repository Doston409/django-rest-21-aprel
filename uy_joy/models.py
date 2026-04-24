from django.db import models


class Apartment(models.Model):
    uy_raqami = models.IntegerField()
    xonalar_soni = models.IntegerField()
    maydoni = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qavat = models.IntegerField()
    narxi = models.IntegerField(default=0)

    def __str__(self):
        return f"Uy {self.uy_raqami}"


class Building(models.Model):
    nomi = models.CharField(max_length=255)
    qavatlar_soni = models.IntegerField()
    qurilgan_yili = models.IntegerField()
    manzili = models.CharField(max_length=255)
    turi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Land(models.Model):
    maydoni = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    turi = models.CharField(max_length=100)
    manzili = models.CharField(max_length=255)
    kadastr_raqami = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.kadastr_raqami