from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length = 20)
    epass = models.CharField(max_length=20)
    esal = models.FloatField()

    @classmethod
    def login(cls,request,obj):
        request.session['empid']=obj.eno

    @classmethod
    def logout(cls,request):
        request.session['empid']=None
