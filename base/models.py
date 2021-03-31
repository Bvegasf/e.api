from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class BaseModel(models.Model):
    

    # TODO: Define fields here
    id=models.AutoField(primary_key=True)
    state=models.BooleanField('estado',default=True)

    # se pone auto_now_add para guardar la fecha de creacion

    created_date=models.DateField('fecha de creacion',auto_now=False,auto_now_add=True)

    # se pone auto_now para guardar la fecha actual de modiciacion

    modified_date =models.DateField('fecha de modificacion',auto_now=True, auto_now_add=False)

    delete_date=models.DateField('Fecha de eliminacion',auto_now=True,auto_now_add=False )

    class Meta:
        abstract= True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Bases'