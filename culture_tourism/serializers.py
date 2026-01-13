from rest_framework import serializers
from .models import Cities, Tourism, TripPlanner, CultureAndTradition, Food

class TripPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlanner
        fields = '__all__'

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

class TourismListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourism
        fields = ['id', 'name', 'image', 'city']

class TourismDetailSerializer(serializers.ModelSerializer):
    trip_planner = TripPlannerSerializer(many=True, read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model = Tourism
        fields = ['id', 'name', 'image', 'about', 'history', 'location', 'city', 'city_name', 'trip_planner']

class CultureAndTraditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureAndTradition
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
