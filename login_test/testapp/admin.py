from django.contrib import admin
from testapp.models import Entry
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display=['title','slug','content','created_by','created_date']
admin.site.register(Entry,EntryAdmin)
