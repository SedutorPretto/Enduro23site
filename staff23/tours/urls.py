from django.urls import path
from .views import VehicleListView, VehicleDetailView, VehicleCreateView, VehicleUpdateView,VehicleDeleteView
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cats/', views.cats, name='cats'),
    path('vehicles/', VehicleListView.as_view(), name='vehicles'),
    path('vehicles/create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicles/<str:slug>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicles/<str:slug>/update/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicles/<str:slug>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete')
]
