from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task
from admin_panel.serializers import AndroidAppSerializer
from admin_panel.models import AndroidApp

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_image', 'points_earned', 'tasks_completed']

class TaskSerializer(serializers.ModelSerializer):
    # Nested representation of the AndroidApp for read operations.
    app = AndroidAppSerializer(read_only=True)
    # Write-only field to accept an AndroidApp ID as input.
    app_id = serializers.PrimaryKeyRelatedField(
        queryset=AndroidApp.objects.all(),
        write_only=True,
        source='app'
    )
    
    class Meta:
        model = Task
        fields = ['id', 'app', 'app_id', 'screenshot', 'created_at', 'approved']
    
    def validate_screenshot(self, value):
        # Add any custom validation for the screenshot here.
        # For example, you can limit file size or check file type.
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'points_earned', 'tasks_completed']
