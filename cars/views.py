from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from Easy_Ride_Backend.utils import get_logger, success_response, error_response
from .models import Car, Brand
from .serializers import CarSerializer, DetailCarSerializer, BrandSerializer
import random

logger = get_logger(__name__)


@api_view(['GET'])
@permission_classes([AllowAny])
def car_list(request):
    try:
        all_cars = Car.objects.all()
        car_list = random.sample(list(all_cars), min(len(all_cars), 10))
        serializer = CarSerializer(car_list, many=True)
        return success_response(serializer.data, message="Data fetched successfully")
    except Exception as e:
        return error_response(error_message="Fetching data failed", error=str(e))
    # except Car.DoesNotExist:
    #     logger.error("No cars found in the database.")
    #     return Response(
    #         {"error": "No cars found in the database."},
    #         status=status.HTTP_404_NOT_FOUND
    #     )
    # except Exception as e:
    #     logger.error(f"Error retrieving random cars: {str(e)}")
    #     return Response(
    #         {"error": "An error occurred while retrieving cars."},
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #     )


@api_view(['POST'])
@permission_classes([AllowAny])
def all_car_list(request):
    filtered_brands = request.data.get('brands')
    try:
        if filtered_brands:
            brands = Brand.objects.filter(name__in=filtered_brands)
            cars = Car.objects.filter(brand__in=brands)
        else:
            cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return success_response(serializer.data, message="Data fetched successfully")
        # return Response(serializer.data, status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error retrieving filtered cars: {e}")
        return error_response(error_message="Fetching data failed", error=str(e))


@api_view(['GET'])
@permission_classes([AllowAny])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = DetailCarSerializer(car)
        return success_response(serializer.data, message="Data fetched successfully")
    # except car.DoesNotExist:
    #     return Response("Car not Found", status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error retrieving car details for PK {pk}: {e}")
        return error_response(error_message="Fetching data failed", error=str(e))


@api_view(['GET'])
@permission_classes([AllowAny])
def car_brands(request):
    try:
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return success_response(serializer.data, message="Data fetched successfully")

    except Exception as e:
        logger.error(f"Error retrieving car brands: {e}")
        return error_response(error_message="Fetching data failed", error=str(e))
