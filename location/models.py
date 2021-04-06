from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class ContinentalRegion(models.Model):
    name = models.CharField('nombre', max_length=230, unique = True)
    name_corto = models.CharField('nombre corto', max_length= 5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Region Continental'



class Country(models.Model):
    name = models.CharField('nombre', max_length= 230, unique= True)
    code = models.CharField('codigo', primary_key= True, max_length=200)
    continental_region= models.ForeignKey(ContinentalRegion, on_delete=CASCADE, null= True, blank= True)

    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = 'Pais'



class City(models.Model):
    name = models.CharField('nombre',max_length=230)
    country = models.ForeignKey(Country, on_delete=CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ciudad'


        

