from django.db import models


class Category(models.Model):
    nomi = models.CharField(max_length=50)
    tavsifi = models.TextField(blank=True, null=True)
    rasm_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nomi


class Product(models.Model):
    nomi = models.CharField(max_length=255)
    kodi = models.IntegerField(default=0)
    narxi = models.IntegerField(default=0)
    miqdori = models.IntegerField(default=0)
    ishlab_chiqaruvchi = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nomi


class Customer(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    telefon = models.CharField(max_length=20)
    manzili = models.TextField(blank=True, null=True)
    jami_xaridi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class Order(models.Model):
    mijoz = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    umumiy_summa = models.IntegerField(default=0)
    tolov_turi = models.CharField(max_length=50)

    def __str__(self):
        return f"Order #{self.id}"


class Supplier(models.Model):
    kompaniya_nomi = models.CharField(max_length=150)
    masul_shaxs = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    yetkazish_muddati = models.CharField(max_length=255, default="1 kun")

    def __str__(self):
        return self.kompaniya_nomi