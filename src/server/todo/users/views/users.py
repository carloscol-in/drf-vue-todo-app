"""Users views."""

# DRF

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins, status, viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# Models
from todo.users.models import User

# Serializers
from todo.users.serializers import UserModelSerializer, UserSignupSerializer, UserLoginSerializer

# Authentication
from todo.users.authentication import EmailOrUsernameAuthentication


class UserViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet,
    ):
    """User view set.
    
    This viewset will handle login, signup and user patch/update."""

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'
    authentication_classes = (EmailOrUsernameAuthentication,)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User's signup view."""

        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, refresh, access = serializer.save()
        user_data = UserModelSerializer(user).data

        data = {
            'user': user_data,
            'refresh_token': str(refresh),
            'access_token': str(access),
        }

        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def login(self, request):
        """Login a user upon GET request."""

        # ? is it good practice to have this here instead of passing it to the UserLoginSerializer?
        # TODO: try to pass the authentication to the UserLoginSerializer validate method
        # * one way could be to override CustomAuthentication().authenticate() params
        # * instead of being `request`, use data dict
        user, _ = EmailOrUsernameAuthentication().authenticate(request)
        user_dict = UserModelSerializer(user).data
        user_dict.update({'password': request.data['password']})
        serializer = UserLoginSerializer(data=user_dict)
        serializer.is_valid(raise_exception=True)
        user, refresh, access = serializer.save()

        data = {
            'user': UserModelSerializer(user).data,
            'refresh_token': refresh,
            'access_token': access,
        }

        return Response(data, status=status.HTTP_200_OK)