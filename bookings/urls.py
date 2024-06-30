from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create-booking'),
    path('user/', views.user_bookings, name='user-bookings'),
]