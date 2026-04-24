from django.db import models


class Doctor(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    mutaxassisligi = models.CharField(max_length=100)
    xona_raqami = models.IntegerField()
    tajribasi = models.IntegerField(default=1)

    def __str__(self):
        return self.ismi


class Patient(models.Model):
    ismi = models.CharField(max_length=255)
    familiyasi = models.CharField(max_length=255)
    kasallik_tarixi = models.TextField()
    qon_guruhi = models.CharField(max_length=10)
    yoshi = models.IntegerField(default=0)

    def __str__(self):
        return self.ismi


class Appointment(models.Model):
    bemor = models.ForeignKey(Patient, on_delete=models.CASCADE)
    shifokor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    sana = models.DateField()
    vaqt = models.TimeField()
    shikoyati = models.TextField()

    def __str__(self):
        return "Qabul"


class Medicine(models.Model):
    nomi = models.CharField(max_length=255)
    dozasi = models.CharField(max_length=100)
    turi = models.CharField(max_length=100)
    muddati = models.CharField(max_length=100)
    qollash_usuli = models.TextField()

    def __str__(self):
        return self.nomi