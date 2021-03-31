from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields.files import ImageField

from base.models import BaseModel

# Create your models here.
class MeasureUnit(BaseModel):
   description= models.CharField(max_length=100, blank=False,null=False, unique=True)
  

   # Propiedades necesarias para que simple history guarde registro de usuarios

   @property
   def _history_user(self):
       return self.changed_by

   @_history_user.setter
   def _history_user(self,value):
        self.changed_by = value



   class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

   def __str__(self):
       return self.description

class CategoryProduct(BaseModel):
    name=models.CharField('nombre',max_length=20,null=False,blank=False)
    description=models.CharField('descripcion',max_length=50,null=False,blank=False)
   

    class Meta:
        verbose_name='Categoria de Producto'
        verbose_name_plural='Categorias de Productos'

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descuent_value=models.PositiveIntegerField(default=0)
    category_product=models.ForeignKey(CategoryProduct,on_delete=CASCADE,verbose_name='indicador de oferta')

    class Meta:
       

        verbose_name = 'Indicador de descuento'
        verbose_name_plural = 'Indicadores de descuentos'

    def __str__(self):
      
        return f'Oferta de la categoria {self.category_product}: {self.descuent_value}%'

class Products(BaseModel):
    name=models.CharField('Nombre de Producto', max_length=100,unique=True,blank=False,null=False)
    description=models.CharField('Descripcion del producto',max_length=50)
    image_product = models.ImageField(upload_to='products/',blank=True,null=True)
    measure_unit=models.ForeignKey(MeasureUnit, on_delete=models.CASCADE,verbose_name='Unidad de medida', null=True)
    category_product=models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name='Categoria de Producto', null=True)


    
    

    
    class Meta:
        verbose_name='Productos'
        verbose_name_plural='Productos'
    def __str__(self):
        return self.name
       
     

