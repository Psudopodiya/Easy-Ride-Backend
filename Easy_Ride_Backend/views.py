# your_app/views.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import status
from Easy_Ride_Backend.utils import success_response, error_response


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            return success_response(data=data, message="Login successful")
        except Exception as e:
            return error_response(error_message="Login failed", error=str(e), status_code=status.HTTP_401_UNAUTHORIZED)


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            return success_response(data=data, message="Token refreshed successfully")
        except Exception as e:
            return error_response(error_message="Token refresh failed", error=str(e),
                                  status_code=status.HTTP_401_UNAUTHORIZED)
