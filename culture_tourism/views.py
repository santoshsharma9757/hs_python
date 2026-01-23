from rest_framework import generics, permissions
from .models import Cities, Tourism, CultureAndTradition, Food, TripPlanner
from .serializers import (
    CitiesSerializer, 
    TourismListSerializer, 
    TourismDetailSerializer,
    CultureAndTraditionSerializer,
    FoodSerializer,
    TripPlannerSerializer
)

class CitiesListAPIView(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [permissions.AllowAny]

class TourismListAPIView(generics.ListAPIView):
    serializer_class = TourismListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Tourism.objects.all()
        city_id = self.request.query_params.get('city_id')
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        return queryset

class TourismDetailAPIView(generics.RetrieveAPIView):
    queryset = Tourism.objects.all()
    serializer_class = TourismDetailSerializer
    permission_classes = [permissions.AllowAny]

class CultureAndTraditionListAPIView(generics.ListAPIView):
    queryset = CultureAndTradition.objects.all()
    serializer_class = CultureAndTraditionSerializer
    permission_classes = [permissions.AllowAny]

class CultureAndTraditionDetailAPIView(generics.RetrieveAPIView):
    queryset = CultureAndTradition.objects.all()
    serializer_class = CultureAndTraditionSerializer
    permission_classes = [permissions.AllowAny]

class FoodListAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]

class FoodDetailAPIView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]

class TripPlannerListAPIView(generics.ListAPIView):
    serializer_class = TripPlannerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = TripPlanner.objects.all()
        tourism_id = self.request.query_params.get('tourism_id')
        if tourism_id:
            queryset = queryset.filter(tourism_id=tourism_id)
        return queryset

class TripPlannerDetailAPIView(generics.RetrieveAPIView):
    queryset = TripPlanner.objects.all()
    serializer_class = TripPlannerSerializer
    permission_classes = [permissions.AllowAny]
