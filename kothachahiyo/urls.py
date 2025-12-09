from django.urls import path
from .views import RoomView

urlpatterns = [
    path("room/", RoomView.as_view(), name="room_data"),
    path("room/<int:pk>/", RoomView.as_view(), name="room_detail"),
]
