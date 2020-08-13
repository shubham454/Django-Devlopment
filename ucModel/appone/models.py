from django.db import models

# Create your models here.
class Uni(models.Model):
    uname = models.CharField(max_length = 50)
    def __str__(self):
        return self.uname

class Col(models.Model):
    cname = models.CharField(max_length = 50)
    uname = models.ForeignKey(Uni, on_delete = models.CASCADE)
    def __str__(self):
        return self.cname
