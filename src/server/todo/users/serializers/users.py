"""Users serializers."""

# DRF
from rest_framework import serializers

# Django
from django.contrib.auth import get_user_model
User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        model = User
        fields = ('username', 'email',)