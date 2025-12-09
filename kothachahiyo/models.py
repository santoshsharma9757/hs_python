from django.db import models
from django.contrib.auth.models import User


class District(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="cities"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.district.name}"


class Location(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    full_address = models.TextField()

    def __str__(self):
        return f"{self.district} {self.city} {self.full_address}"


class Room(models.Model):
    FURNISHED_CHOICE = (
        ("furnished", "Furnished"),
        ("unfurnished", "Unfurnished"),
        ("semi-furnished", "Semi-Furnished"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_furnished = models.CharField(
        max_length=50, choices=FURNISHED_CHOICE, default="unfurnished"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True, blank=True
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_images")
    image = models.ImageField(upload_to="room/images/")
