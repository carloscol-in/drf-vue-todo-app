"""Users serializers."""

# DRF
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# Django
from django.db import IntegrityError
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model, password_validation, authenticate
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

class UserLoginSerializer(serializers.Serializer):
    """User login serializer."""

    username = serializers.CharField()
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )

    # First, validate there's a user with that email and the password
    # is set to the password passed to the serializer.
    # Secondly, create refresh and access tokens.

    def validate(self, data):
        """Validate email and password are part of a single user."""
        user = User.objects.get(username=data['username'])
        self.context['user'] = user
        return data

    def create(self, data):
        """Return user from context, refresh and access tokens."""

        user = self.context['user']

        refresh = str(TokenObtainPairSerializer().get_token(user))
        access = str(AccessToken().for_user(user))

        return (user, refresh, access)

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

    def validate(self, data):
        """Validate password against password validations on settings."""
        password = data['password']
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Override create method to create the user and perform any actions."""

        try:
            user = User.objects.create_user(**data, is_verified=False)
        except IntegrityError:
            raise serializers.ValidationError('Username or Email already exists.')


        refresh = str(TokenObtainPairSerializer().get_token(user))
        access = str(AccessToken().for_user(user))

        # ? send email for verification?

        return (user, refresh, access)