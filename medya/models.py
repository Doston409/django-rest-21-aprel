from django.db import models


class Song(models.Model):
    nomi = models.CharField(max_length=255)
    ijrochi = models.CharField(max_length=255)
    janri = models.CharField(max_length=255)
    davomiyligi = models.IntegerField(default=0)
    yili = models.IntegerField(default=1)

    def __str__(self):
        return self.nomi


class Book(models.Model):
    nomi = models.CharField(max_length=255)
    muallif = models.CharField(max_length=255)
    betlar_soni = models.IntegerField(default=0)
    janri = models.CharField(max_length=255)
    nashriyot = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Exhibition(models.Model):
    nomi = models.CharField(max_length=255)
    sana = models.DateField()
    chipta_narxi = models.IntegerField(default=0)
    mavzusi = models.CharField(max_length=255)
    tashkilotchi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class Podcast(models.Model):
    nomi = models.CharField(max_length=255)
    mavzusi = models.CharField(max_length=255)
    muallif = models.CharField(max_length=255)
    qismlar_soni = models.IntegerField(default=1)
    platforma = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi