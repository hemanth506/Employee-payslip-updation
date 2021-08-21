from django.db import models

# Create your models here.

class Payslip(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pan = models.IntegerField()
    uan = models.IntegerField()
    basic_pay = models.IntegerField()
    benefites = models.IntegerField()
    Taxes = models.FloatField()

    def __str__(self):
        return self.name

class SetTaxes(models.Model):
    taxPercent = models.FloatField()

    def __int__(self):
        return float(self.taxPercent)

