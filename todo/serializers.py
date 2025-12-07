"""
Todo Serializers
Converts Todo model instances to/from JSON format
Serializers handle data validation and transformation
"""

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Todo Serializer
    Handles serialization (Python object -> JSON) and deserialization (JSON -> Python object)

    Fields:
    - id: Auto-generated unique identifier (read-only)
    - title: Todo item title (required, max 50 characters)
    - description: Detailed description of the todo (required)
    - created_at: Timestamp when todo was created (read-only, auto-generated)
    - user: The user who owns this todo (read-only, set automatically from request)
    """

    class Meta:
        # Specify which model this serializer works with
        model = Todo

        # List all fields that should be included in the API response
        # These fields will be converted to/from JSON
        fields = ["id", "title", "description", "created_at", "user"]

        # Read-only fields cannot be set by the user in POST/PUT requests
        # They are automatically set by the system
        read_only_fields = ["id", "created_at", "user"]

    # You can add custom validation here if needed
    # For example, to ensure title is not empty:
    def validate_title(self, value):
        """
        Custom validation for title field
        Ensures title is not just whitespace
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value.strip()
