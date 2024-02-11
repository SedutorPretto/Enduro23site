from django.urls import path

from .views import ProfileUpdateView, ProfileDetailView, UserLoginView, UserLogoutView


urlpatterns = [
    path('user/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
