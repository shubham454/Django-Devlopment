from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','epass','esal']

admin.site.register(Employee,EmployeeAdmin)
