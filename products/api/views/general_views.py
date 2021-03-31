# vistas genericas del frmaework

# from rest_framework import generics

#importacion de los modelos
# se importa para aumentar la astraccion y no usar 3 veces el get.queryset()
from rest_framework import viewsets
from base.api import GeneraListApiView

from products.api.serializer.general_serializer import MeasureUnitserializer,CategoryProductserializer,Indicatorserializer

# La clase de la vista hereda de generics la clase que django tiene predeterminada(ListAPIView)

class MeasureUnitViewSet(viewsets.ModelViewSet):

    #se le debe indicar el serializador al cual pertenece

    serializer_class=MeasureUnitserializer

    #luego se realiza la consulta Queryset   

class IndicatorViewSet(viewsets.ModelViewSet):

    serializer_class=Indicatorserializer    

class CategoryProductViewSet(viewsets.ModelViewSet):

    serializer_class=CategoryProductserializer
    




