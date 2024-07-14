from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Car, Brand
from .serializers import CarSerializer, DetailCarSerializer, BrandSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def car_list(request):
    cars = Car.objects.all()[0:10]
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def all_car_list(request):
    filtered_brands = request.data.get('brands')
    print(filtered_brands)
    if len(filtered_brands) > 0:
        brand = Brand.objects.filter(name__in=filtered_brands)
        cars = Car.objects.filter(brand__in=brand)
    else:
        cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=404)
    serializer = DetailCarSerializer(car)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def car_brands(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)

