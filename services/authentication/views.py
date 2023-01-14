from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from libs.request_event import snake_to_camel_dict
from services.users.serializers import UserRetrieveSerializer


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(
            email=email,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)

            if login_serializer.is_valid():
                user_serializer = UserRetrieveSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refreshToken': login_serializer.validated_data.get('refresh'),
                    'user': snake_to_camel_dict(user_serializer.data),
                }, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_401_UNAUTHORIZED)
