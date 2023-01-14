from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from services.users.serializers import UserRetrieveSerializer
from libs.request_event import snake_to_camel_dict


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        print(email)
        print(password)

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
            return Response({'ok': False, 'message': 'Email or password wrong'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'ok': False, 'message': 'User does not exist or wrong login info'}, status=status.HTTP_400_BAD_REQUEST)
