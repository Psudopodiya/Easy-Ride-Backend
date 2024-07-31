from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from .serializers import CustomUserSerializer
from Easy_Ride_Backend.utils import get_logger
from rest_framework.response import Response

logger = get_logger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    except ValidationError as e:

        # Handle validation errors explicitly
        error_details = e.detail
        if isinstance(error_details, dict):
            first_error = next(iter(error_details.values()))
            if isinstance(first_error, list) and first_error:
                first_error_message = str(first_error[0])
            else:
                first_error_message = str(first_error)
        else:
            first_error_message = str(error_details)

        return Response(
            {'error': 'Validation failed', 'details': first_error_message},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        logger.error(f"Unexpected error in user registration: {str(e)}")
        return Response(
            {'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status.HTTP_200_OK)
