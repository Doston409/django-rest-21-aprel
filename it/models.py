from django.db import models


class Project(models.Model):
    nomi = models.CharField(max_length=255)
    muddat = models.DateField()
    byudjet = models.IntegerField(default=0)
    masul_shaxs = models.CharField(max_length=255)
    holati = models.CharField(max_length=255, default="yangi")

    def __str__(self):
        return self.nomi


class BugReport(models.Model):
    loyiha_nomi = models.CharField(max_length=255)
    xatolik_tavsifi = models.TextField()
    jiddiylik_darajasi = models.CharField(max_length=255)
    topilgan_sana = models.DateField()

    def __str__(self):
        return self.loyiha_nomi


class Laptop(models.Model):
    brend = models.CharField(max_length=255)
    protsessor = models.CharField(max_length=255)
    ram_hajmi = models.IntegerField(default=0)
    xotira = models.CharField(max_length=255, default="GB")
    narxi = models.IntegerField(default=0)

    def __str__(self):
        return self.brend