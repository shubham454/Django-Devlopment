from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['ename','eaddress','esalary','experience','gender']
admin.site.register(Employee,EmployeeAdmin)
