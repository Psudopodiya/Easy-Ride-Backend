from datetime import datetime
from typing import Dict, Any
from Easy_Ride_Backend.utils import get_logger, success_response, error_response
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from cars.models import Car
from .serializers import BookingSerializer
from rest_framework import status

logger = get_logger(__name__)


def parse_date(date_string: str) -> datetime.date:
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("Invalid date format. Use YYYY-MM-DD.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    """
        Create a new booking for an authenticated user.
    """
    print(request.data)
    car_id = request.data.get('car_id')
    start_date = request.data.get("start_date")
    end_date = request.data.get("end_date")
    try:
        car = Car.objects.get(id=car_id)
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)

        if start_date >= end_date:
            raise ValidationError("End date must be after start date")

        booking_days = (end_date - start_date).days + 1
        total_cost = booking_days * car.rental_rate

        booking_data: Dict[str, Any] = {
            'car': car.id,
            'start_date': start_date,
            'end_date': end_date,
            'total_cost': total_cost
        }

        serializer = BookingSerializer(data=booking_data)
        if serializer.is_valid(raise_exception=True):
            booking = serializer.save(user=request.user)
            car.is_booked = True
            car.save()
            return success_response(serializer.data, message="Booking created successfully", status_code=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(f"Error retrieving car brands: {e}")
        return error_response(error_message="Booking failed", error=str(e))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_bookings(request):
    try:
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return success_response(serializer.data)
    except Exception as e:
        return error_response(error_message="Fetching data failed", error=str(e))
