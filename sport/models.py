from django.db import models


class Athlete(models.Model):
    ismi = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    sport_turi = models.CharField(max_length=255)
    boyi = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    vazni = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.ismi} {self.familiya}"


class Gym(models.Model):
    nomi = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)
    oylik_abonement_narxi = models.IntegerField(default=0)
    ish_vaqti = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Competition(models.Model):
    nomi = models.CharField(max_length=255)
    sana = models.DateField()
    mukofot_jamgarmasi = models.IntegerField(default=0)
    manzili = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Coach(models.Model):
    ismi = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    tajribasi = models.IntegerField(default=0)
    ixtisosligi = models.CharField(max_length=255)
    oylik_maosh = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.ismi} {self.familiya}"