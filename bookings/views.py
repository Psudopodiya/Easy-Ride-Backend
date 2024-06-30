from datetime import datetime
from typing import Dict, Any
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from cars.models import Car
from .serializers import BookingSerializer


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

    car_name = request.data.get('car')
    start_date = request.data.get("start_date")
    end_date = request.data.get("end_date")

    if not all([car_name, start_date, end_date]):
        return Response({"error": "Please provide car, start_date, and end_date"}, status=400)

    try:
        car = Car.objects.get(name=car_name)
        if car.is_booked:
            return Response({"error": "The Car is already booked select some other car "})
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
            return Response(serializer.data, status=210)
    except Car.DoesNotExist:
        return Response(
            {"error": f"Car '{car_name}' not found"},
            status=404
        )
    except ValidationError as e:
        return Response({"error": str(e)}, status=400)
    except Exception as e:
        return Response(
            {"error": "An unexpected error occurred"},
            status=500
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
