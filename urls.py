from django.urls import path
from . import views

urlpatterns = [
    path('bike_rental/', views.bike_rental, name='bike_rental'),
]