from django.db import models

# Create your models here.
class Employee(models.Model):
    choice = [('MALE', 'male'),('FEMALE', 'female')]
    ename = models.CharField(max_length = 10, unique=True)
    eaddress = models.CharField(max_length = 20)
    esalary = models.FloatField()
    experience = models.FloatField()
    gender = models.CharField(max_length=10,choices = choice, default='MALE')
    image = models.FileField(upload_to='media',null=True)

    @classmethod
    def login(cls,request,emp):
        request.session['empid']=emp.ename

    @classmethod
    def logout(cls,request):
        request.session['empid']=None
