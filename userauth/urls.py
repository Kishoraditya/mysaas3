# userauth/urls.py
from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, CustomPasswordResetView, ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='account_profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    
]
