from django.contrib import admin
from empleado.models import *

# Register your models here.

class departmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(Department, departmentAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Employee)
