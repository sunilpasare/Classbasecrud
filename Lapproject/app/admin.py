from django.contrib import admin
from .models import Laptop

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display=['id','Modelname','Company','Ram','Rom','Weight','Processor']

admin.site.register(Laptop,LaptopAdmin)



