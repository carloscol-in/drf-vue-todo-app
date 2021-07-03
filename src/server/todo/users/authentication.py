"""Custom users authentication."""

# DRF
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

# Django
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class EmailOrUsernameAuthentication(BaseAuthentication):
    """Authenticate by using either email or username."""

    def authenticate(self, request):
        """Override authenticate method."""

        # import pdb; pdb.set_trace()

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        auth_type = settings.AUTH_AUTHENTICATION_TYPE

        if not username and not password:
            return None

        if auth_type == 'username':
            return super().authenticate(username, password)

        try:
            if auth_type == 'both':
                user = User.objects.get(
                    Q(username__iexact=username) | Q(email__iexact=username)
                )
            else:
                user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            # raise exceptions.AuthenticationFailed('Invalid user credentials.')
            raise exceptions.AuthenticationFailed('No such user.')
        else:
            # import pdb; pdb.set_trace()
            if user.check_password(password):
                return (user, None)
            else:
                raise exceptions.AuthenticationFailed("Invalid user credentials.")