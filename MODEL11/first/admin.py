from django.contrib import admin
from first.models import BankAccount

# Register your models here.
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['ano','name','add']

admin.site.register(BankAccount,BankAccountAdmin)