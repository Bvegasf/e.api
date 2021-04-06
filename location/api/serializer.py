from location.models import City, ContinentalRegion, Country
from rest_framework import serializers



class ContinentalRegionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContinentalRegion
        fields = '__all__'


class CountryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class CityModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
