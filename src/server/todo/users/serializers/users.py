"""Users serializers."""

# DRF
from rest_framework import serializers, exceptions

# Django
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )

class UserSignupSerializer(serializers.Serializer):
    """User signup serializer."""

    # user
    username = serializers.CharField(
        min_length=4,
        max_length=50,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # contact
    email = serializers.EmailField(
        min_length=4,
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # password
    password = serializers.CharField(
        min_length=8,
        max_length=64,
    )

    def create(self, data):
        """Create user."""

        # import pdb; pdb.set_trace()

        try:
            user = User.objects.create_user(**data, is_verified=False)
        except IntegrityError as e:
            raise serializers.ValidationError('Username or Email already exists.')

        # ? send email for verification?

        return user