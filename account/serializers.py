from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True, required=False)   # NEW

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "role"]

    def create(self, validated_data):
        role = validated_data.pop("role", None)
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)

        if role == "admin":
            user.is_staff = True
            user.is_superuser = True

        user.save()
        return user

