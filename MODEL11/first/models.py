from django.db import models
# Create your models here.
class BankAccount(models.Model):
    ano = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    add = models.CharField(max_length=50)
