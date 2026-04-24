from django.db import models


class Dish(models.Model):
    nomi = models.CharField(max_length=255)
    tarkibi = models.TextField()
    narxi = models.IntegerField(default=0)
    kaloriyasi = models.IntegerField(default=0)
    tayyorlanish_vaqti = models.IntegerField(default=0)

    def __str__(self):
        return self.nomi


class Waiter(models.Model):
    ismi = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    stol_raqamlari = models.CharField(max_length=255)
    tajribasi = models.IntegerField(default=0)
    reytingi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ismi} {self.familiya}"


class Table(models.Model):
    raqami = models.IntegerField(default=0)
    orinqlar_soni = models.IntegerField(default=0)
    holati = models.BooleanField(default=False)
    qavat = models.IntegerField(default=0)

    def __str__(self):
        return f"Stol {self.raqami}"