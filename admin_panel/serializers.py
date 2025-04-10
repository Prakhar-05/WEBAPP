from rest_framework import serializers
from .models import AndroidApp

class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = ['id', 'name', 'description', 'download_url', 'points', 'created_at']
