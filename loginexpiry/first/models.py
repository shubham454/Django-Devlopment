from django.db import models
from django.shortcuts import render,reverse

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=50)
    email=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('list', kwargs={'pk': self.pk})
