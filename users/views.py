from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from Easy_Ride_Backend.utils import get_logger

logger = get_logger(__name__)


def handle_validation_error(e: ValidationError) -> Response:
    """Helper function to handle validation errors and return a formatted response."""
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
        {"detail": first_error_message, "code": "validation_error"},
        status=status.HTTP_400_BAD_REQUEST
    )


def handle_unexpected_error(e: Exception, context: str) -> Response:
    """Helper function to handle unexpected errors and return a formatted response."""
    logger.error(f"Unexpected error in {context}: {str(e)}")
    return Response(
        {"detail": "An unexpected error occurred", "code": "server_error"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return handle_validation_error(e)
    except Exception as e:
        return handle_unexpected_error(e, "user registration")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    try:
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValidationError as e:
        return handle_validation_error(e)
    except Exception as e:
        return handle_unexpected_error(e, "retrieving user data")
