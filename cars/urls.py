from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car-list'),
    path('all-car-list/', views.all_car_list, name='all-list'),
    path('<int:pk>/', views.car_detail, name='car-detail'),
    path('brands/', views.car_brands, name='car-brands'),
]