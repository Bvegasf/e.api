from django.db import models
from django.db.models import fields
from products.models import MeasureUnit,CategoryProduct,Indicator

from rest_framework import serializers

class MeasureUnitserializer(serializers.ModelSerializer):
    class Meta:
        model=MeasureUnit
        exclude=('state','created_date','modified_date','delete_date')

class CategoryProductserializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryProduct
        fields='__all__'

class Indicatorserializer(serializers.ModelSerializer):
    class Meta:
        model=Indicator
        fields='__all__'