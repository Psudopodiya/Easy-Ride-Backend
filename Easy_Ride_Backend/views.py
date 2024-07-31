from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from Easy_Ride_Backend.utils import get_logger
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

logger = get_logger(__name__)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except TokenError as e:
            logger.warning(f"Token error: {str(e)}")
            return Response(
                {'error': 'Invalid token', 'details': str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except InvalidToken as e:
            logger.warning(f"Invalid token: {str(e)}")
            return Response(
                {'error': 'Invalid credentials', 'details': str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            logger.error(f"Unexpected error in token obtain: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Response(response.data, status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Unexpected error in token obtain: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )