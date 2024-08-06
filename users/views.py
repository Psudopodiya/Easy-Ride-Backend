from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import CustomUserSerializer
from Easy_Ride_Backend.utils import get_logger, success_response, error_response

logger = get_logger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return success_response(serializer.validated_data, message="Registration successful")
    except Exception as e:
        error_details = serializer.errors
        error_message = ''
        for field, errors in error_details.items():
            error_message = errors[0]
        return error_response(
            error_message="Registration Failed", error=str(error_message), status_code=status.HTTP_401_UNAUTHORIZED
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    try:
        serializer = CustomUserSerializer(request.user)
        return success_response(serializer.data, message="User Data successful")
    except Exception as e:
        return error_response(
            error_message="Error in retrieving user data", error=str(e), status_code=status.HTTP_401_UNAUTHORIZED
        )
