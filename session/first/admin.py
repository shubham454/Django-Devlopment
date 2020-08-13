from django.contrib import admin
from .models import ItemAdd
# Register your models here.

class ItemAddAdmin(admin.ModelAdmin):
    list_display = ['name','quantity']

admin.site.register(ItemAdd,ItemAddAdmin)
