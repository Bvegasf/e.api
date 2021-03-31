from django.contrib import admin
from products.models import Products,CategoryProduct, MeasureUnit,Indicator

# Register your models here.

class MesaureUnitAdmin(admin.ModelAdmin):
    list_display=('id','description')

class CategoryProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name')


admin.site.register(Products)
admin.site.register(CategoryProduct,CategoryProductAdmin)
admin.site.register(MeasureUnit,MesaureUnitAdmin)
admin.site.register(Indicator)