from django.contrib import admin
from .models import CarMake,CarModel


class CarModelInline(admin.StackedInline):
    model=CarModel
    extra=5

class CarModelAdmin(admin.ModelAdmin):
    list_display=['name', 'dealer_id','Type','year']

class CarMakeAdmin(admin.ModelAdmin):
    inlines=[CarModelInline]
    list_display=['name','description']

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
