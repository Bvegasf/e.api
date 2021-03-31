from products.models import CategoryProduct, Products
from rest_framework import fields, serializers
from products.api.serializer.general_serializer import MeasureUnitserializer,CategoryProductserializer

class Productsserializer(serializers.ModelSerializer):

  

    class Meta:
        model=Products
        exclude=('state','created_date','modified_date','delete_date')

    def to_representation(self, instance):

        return {
            'id':instance.id,
            'name':instance.name,
            'description':instance.description,
            'image_product': instance.image_product if instance.image_product != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.name if instance.category_product is not None else ''
        }