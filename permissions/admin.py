from permissions.models import Role
from django.contrib import admin
from permissions.models import Role, Permissions

# Register your models here.
admin.site.register(Role)
admin.site.register(Permissions)