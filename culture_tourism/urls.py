from django.urls import path
from .views import (
    CitiesListAPIView,
    TourismListAPIView,
    TourismDetailAPIView,
    CultureAndTraditionListAPIView,
    CultureAndTraditionDetailAPIView,
    FoodListAPIView,
    FoodDetailAPIView,
    TripPlannerListAPIView,
    TripPlannerDetailAPIView
)

urlpatterns = [
    path('cities/', CitiesListAPIView.as_view(), name='cities-list'),
    path('tourism/', TourismListAPIView.as_view(), name='tourism-list'),
    path('tourism/<uuid:pk>/', TourismDetailAPIView.as_view(), name='tourism-detail'),
    path('culture/', CultureAndTraditionListAPIView.as_view(), name='culture-list'),
    path('culture/<uuid:pk>/', CultureAndTraditionDetailAPIView.as_view(), name='culture-detail'),
    path('food/', FoodListAPIView.as_view(), name='food-list'),
    path('food/<uuid:pk>/', FoodDetailAPIView.as_view(), name='food-detail'),
    path('trip-planner/', TripPlannerListAPIView.as_view(), name='trip-planner-list'),
    path('trip-planner/<uuid:pk>/', TripPlannerDetailAPIView.as_view(), name='trip-planner-detail'),
]
