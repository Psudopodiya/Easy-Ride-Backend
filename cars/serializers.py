from rest_framework import serializers
from .models import Car

from rest_framework import serializers
from .models import Car, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'country_of_origin']


class DetailCarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'rental_rate', 'car_class', 'basic_features', 'additional_features',
                  'year_of_manufacturing', 'rating', 'image', 'is_booked']


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.name
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'rental_rate', 'car_class', 'image', 'basic_features']
