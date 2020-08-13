from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'media/')
    imgname = models.CharField(max_length = 50)
