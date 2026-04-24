from django.db import models


class Motorcycle(models.Model):
    markasi = models.CharField(max_length=255)
    modeli = models.CharField(max_length=255)
    kubaturasi = models.IntegerField(default=0)
    rangi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.markasi} {self.modeli}"


class SparePart(models.Model):
    nomi = models.CharField(max_length=255)
    qaysi_mashinaga = models.CharField(max_length=255)
    zavod_kodi = models.CharField(max_length=50, unique=True)
    narxi = models.IntegerField(default=0)
    kafolati = models.IntegerField(default=0)  

    def __str__(self):
        return self.nomi


class AutoService(models.Model):
    klient_ismi = models.CharField(max_length=255)
    mashina_raqami = models.CharField(max_length=20)
    muammo = models.TextField()
    usta_ismi = models.CharField(max_length=255)
    narxi = models.IntegerField()

    def __str__(self):
        return self.klient_ismi