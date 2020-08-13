from django.db import models

# Create your models here.
class  Dog(models.Model):
    name = models.CharField(max_length = 50)
    life = models.FloatField()
    cost = models.IntegerField()
    def __str__(self):
        return self.name
