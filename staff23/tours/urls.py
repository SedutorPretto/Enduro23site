from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cats/', views.cats, name='cats')
]
