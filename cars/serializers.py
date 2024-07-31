from rest_framework import serializers
from .models import Car, Brand, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image', 'is_cover']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'country_of_origin']


class DetailCarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'rental_rate', 'car_class', 'basic_features', 'additional_features',
                  'description',
                  'year_of_manufacturing', 'rating', 'is_booked', 'images']


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    cover_image = serializers.SerializerMethodField()

    def  get_brand(self, obj):
        return obj.brand.name

    def get_cover_image(self, obj):
        cover_image = obj.images.filter(is_cover=True).first()
        if cover_image:
            return cover_image.image.url
        return None

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'rental_rate', 'car_class', 'cover_image', 'basic_features']
