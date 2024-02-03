from django.urls import path
from .views import VehicleListView, VehicleDetailView
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cats/', views.cats, name='cats'),
    path('vehicles/', VehicleListView.as_view(), name='vehicles'),
    path('vehicles/<str:slug>/', VehicleDetailView.as_view(), name='vehicle_detail')
]
