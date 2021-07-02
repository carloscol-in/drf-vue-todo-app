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
from todo.users.serializers import UserModelSerializer, UserSignupSerializer


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

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User's signup view."""

        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserModelSerializer(user).data


        refresh = TokenObtainPairSerializer().get_token(user)
        access = AccessToken().for_user(user)

        data = {
            'user': user_data,
            'refresh_token': str(refresh),
            'access_token': str(access),
        }

        return Response(data, status=status.HTTP_200_OK)