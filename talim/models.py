from django.db import models


class Group(models.Model):
    nomi = models.CharField(max_length=100)
    yonalishi = models.CharField(max_length=100, blank=True, null=True)
    ochilgan_sana = models.DateField(blank=True, null=True)
    talabalar_soni = models.IntegerField(default=0)

    def __str__(self):
        return self.nomi


class Student(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class Course(models.Model):
    nomi = models.CharField(max_length=150)
    narxi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    davomiyligi = models.IntegerField()
    darajasi = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nomi


class Subject(models.Model):
    nomi = models.CharField(max_length=150)
    dars_soati = models.IntegerField(default=1)
    laboratoriya_borligi = models.BooleanField(default=False)

    def __str__(self):
        return self.nomi


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fan = models.ForeignKey(Subject, on_delete=models.CASCADE)
    baho = models.IntegerField(default=0)
    sana = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.baho}"


class LibraryCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    berilgan_sana = models.DateField()
    amal_qilish_muddati = models.DateField(null=True, blank=True)