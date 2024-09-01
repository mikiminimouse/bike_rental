from django.urls import path
from . import views

urlpatterns = [
    path('bikemodels/', views.bikemodel_list, name='bikemodel_list'),
    path('bikemodel/<int:id>/', views.bikemodel_detail, name='bikemodel_detail'),
]
