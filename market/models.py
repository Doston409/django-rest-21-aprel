from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=233)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=233)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Daraxt(models.Model):
    title = models.CharField(max_length=144)
    price = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.ntitleame
    

