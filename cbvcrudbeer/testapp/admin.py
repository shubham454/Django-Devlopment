from django.contrib import admin
from testapp.models import Beer

# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display = ['name','color','teast','price']

admin.site.register(Beer,BeerAdmin)
