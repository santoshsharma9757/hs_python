"""
Account Views - Handles user registration, login, and logout
This module uses JWT (JSON Web Tokens) for authentication
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate

# Import JWT token classes from SimpleJWT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class RegistrationView(APIView):
    """
    User Registration View
    Allows new users to create an account
    No authentication required - anyone can register
    """

    def post(self, request):
        """
        POST /api/auth/register/

        Request body:
        {
            "username": "john_doe",
            "email": "john@example.com",
            "password": "securepassword123"
        }

        Returns:
        - 201 Created: User successfully registered
        - 400 Bad Request: Validation errors (e.g., username already exists)
        """
        # Validate the incoming data using our serializer
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            # Save the user (serializer handles password hashing)
            serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "user_id": serializer.data.get("id"),
                    "username": serializer.data.get("username"),
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            # Return validation errors if data is invalid
            return Response(
                {"error": "Registration failed", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoginView(APIView):
    """
    User Login View
    Authenticates user and returns JWT tokens
    No authentication required - this is how users get their tokens
    """

    def post(self, request):
        """
        POST /api/auth/login/

        Request body:
        {
            "username": "john_doe",
            "password": "securepassword123"
        }

        Returns:
        - 200 OK: Login successful with access and refresh tokens
        - 400 Bad Request: Invalid credentials
        """
        # Get username and password from request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate that both fields are provided
        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Authenticate the user (Django checks username/password)
        user = authenticate(username=username, password=password)

        if user:
            # If authentication successful, generate JWT tokens
            # RefreshToken is used to generate both access and refresh tokens
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Login successful",
                    # Access token: Short-lived (15 min), use for API requests
                    # Include in header: Authorization: Bearer <access_token>
                    "access": str(refresh.access_token),
                    # Refresh token: Long-lived (7 days), use to get new access tokens
                    # Use this when access token expires
                    "refresh": str(refresh),
                    "user_id": user.id,
                    "username": user.username,
                },
                status=status.HTTP_200_OK,
            )
        else:
            # Authentication failed - wrong username or password
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutView(APIView):
    """
    User Logout View
    Blacklists the refresh token so it can't be used again
    User must be authenticated to logout
    """

    # Use JWT authentication instead of Token authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        POST /api/auth/logout/

        Headers:
        Authorization: Bearer <access_token>

        Request body:
        {
            "refresh": "<refresh_token>"
        }

        Returns:
        - 200 OK: Logout successful, refresh token blacklisted
        - 400 Bad Request: Refresh token not provided or invalid
        """
        try:
            # Get the refresh token from request body
            refresh_token = request.data.get("refresh")

            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Create a RefreshToken object from the string
            token = RefreshToken(refresh_token)

            # Blacklist the token so it can't be used again
            # This is important for security - prevents token reuse after logout
            token.blacklist()

            return Response(
                {"message": "Logged out successfully"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            # Handle invalid or expired tokens
            return Response(
                {"error": "Invalid refresh token", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
