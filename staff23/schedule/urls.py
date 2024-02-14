from django.urls import path
from .views import DateView


urlpatterns = [
    path('schd/', DateView.as_view(), name='test_sc')
]
