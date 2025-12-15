from django.urls import path
from .views import RoomView,DistrictView

urlpatterns = [
    path("room/", RoomView.as_view(), name="room_data"),
    path("room/<int:pk>/", RoomView.as_view(), name="room_detail"),
    path("districts/", DistrictView.as_view(), name='district')
]
