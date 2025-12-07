"""
Account URL Configuration
Defines all authentication-related endpoints
"""

from django.urls import path
from .views import RegistrationView, LoginView, LogoutView
# Import SimpleJWT's built-in views for token management
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Get access and refresh tokens
    TokenRefreshView,     # Get new access token using refresh token
    TokenVerifyView,      # Verify if a token is valid
)

urlpatterns = [
    # Custom views (with detailed responses and comments)
    path('register/', RegistrationView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    
    # SimpleJWT built-in views (standard JWT endpoints)
    # These are production-ready and follow JWT standards
    
    # POST /api/auth/token/ - Get access and refresh tokens
    # Request: {"username": "user", "password": "pass"}
    # Response: {"access": "...", "refresh": "..."}
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # POST /api/auth/token/refresh/ - Get new access token
    # Request: {"refresh": "<refresh_token>"}
    # Response: {"access": "..."}
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # POST /api/auth/token/verify/ - Verify if token is valid
    # Request: {"token": "<access_or_refresh_token>"}
    # Response: {} if valid, 401 if invalid
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]