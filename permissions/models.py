from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=200, unique= True)

    class Meta:

        db_table = 'Roles'



class Permissions(models.Model):
    PERMISSION = {
        'list':False,
        'create':False,
        'update':False,
        'destroy':False,
        }
    role = models.ForeignKey(Role, on_delete=CASCADE)
    is_super = models.BooleanField(default=False)

    class Meta:
        db_table = 'Permission'
