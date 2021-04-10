from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from branch.models import branch
from location.models import ContinentalRegion,Country, City
from location.api.serializer import ContinentalRegionModelSerializer,CountryModelSerializer, CityModelSerializer



class BranchModelserializer(serializers.ModelSerializer):
    class Meta:
        model = branch
        fields = '__all__'




    def to_representation(self, instance):
        """
        if instance.continental_region:
            continental_region = instance.continental_region.name

        if instance.country:
            country = instance.country.name

        if instance.city:
            city = instance.city.name
            """

        return{
            
            'name':instance.name,
            'adress':instance.adress,
            'continental_region':instance.continental_region.name if instance.continental_region is not None else "",
            'country':instance.country.name if instance.country is not None else "",
            'city':instance.city.name if instance.city is not None else ""
        }
            

        