from django.db import models

# Create your models here.

class LoginPage(models.Model):
    user_name = models.CharField(max_length=50)
    parol = models.CharField(max_length=50)

class RegisterPage(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    parol = models.CharField(max_length=50)



