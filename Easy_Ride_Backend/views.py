# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenRefreshSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from Easy_Ride_Backend.utils import get_logger
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError, AuthenticationFailed
#
# logger = get_logger(__name__)
#
#
# class CustomTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         serializer = TokenObtainSerializer(data=request.data)
#         try:
#             if serializer.is_valid(raise_exception=True):
#                 return Response(serializer.validated_data, status=status.HTTP_200_OK)
#         except Exception as e:
#             logger.warning(f"Authentication error: {str(e)}")
#             return Response(
#                 {"detail": str(e), "code": "authentication_failed"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )
#
#
# class CustomTokenRefreshView(TokenRefreshView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = TokenRefreshSerializer(data=request.data)
#         try:
#             if serializer.is_valid():
#                 return Response(serializer.validated_data, status=status.HTTP_200_OK)
#         except Exception as e:
#             logger.warning(f"Authentication error: {str(e)}")
#             return Response(
#                 {"detail": str(e), "code": "authentication_failed"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )
