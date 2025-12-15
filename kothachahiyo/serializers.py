from rest_framework import serializers
from .models import Room, RoomImage, District




class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name"]



class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ["id", "image"]


class RoomSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["id", "title", "content", "is_furnished", "price", "room_images"]
        
    
    
    def validate_price(self,value):
        if value>20000:
            raise serializers.ValidationError('price most not be greater than RS: 20000')
        return value
    
    def validate(self, data):
        if data['title']==data['content']:
            raise serializers.ValidationError('title and content should not be same')
        return data
