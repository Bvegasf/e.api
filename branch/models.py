from django.db import models
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE
from location.models import ContinentalRegion,Country,City

# Create your models here.


class branch(models.Model):
    ECHOMERCH = 'ECHO'
    HIPERMERCH='HIPER'
    MEGAMERCH = 'MEGA'

    names = [(ECHOMERCH,'Echomert'),
    (HIPERMERCH,'Hipermerch'),
    (MEGAMERCH,'Mega')
    ]

    name = models.CharField('nombre', max_length=200,   choices=names ,default=ECHOMERCH)
    continental_region =models.ForeignKey(ContinentalRegion, on_delete=CASCADE, null=True, blank= True)
    country = models.ForeignKey(Country, on_delete=CASCADE, null= True, blank= True)
    city = models.ForeignKey(City, on_delete= CASCADE, null= True, blank= True)
    adress = models.TextField(max_length= 400, blank=True)

    def __str__(self) -> str:
        return f'{self.name} nucleo: {self.city} direccion: {self.adress}'


    class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'


