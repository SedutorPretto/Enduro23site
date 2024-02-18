from django.urls import path
from .views import ScheduleListView


urlpatterns = [
    path('schd/', ScheduleListView.as_view(), name='schedule')
]
