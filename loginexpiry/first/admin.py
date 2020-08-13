from django.contrib import admin
from first.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','ename','email','password']

admin.site.register(Employee,EmployeeAdmin)
