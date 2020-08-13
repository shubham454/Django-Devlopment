from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    title=models.CharField(max_length=256)
    slug=models.CharField(max_length=256)
    content=models.TextField(null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Entry'
        verbose_name_plural='Entries'

    def __unicode__(self):
        return self.title
