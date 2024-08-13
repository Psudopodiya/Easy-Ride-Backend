from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('me/', views.get_user, name='me'),
    path('balance/add/', views.add_balance, name='add-balance'),
]