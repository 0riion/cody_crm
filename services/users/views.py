import email
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from services.users.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)
from services.users.models import User


from services.users.models import User
from services.users.serializers import (
    UserSerializer, UserListSerializer, UpdateUserSerializer,
    PasswordSerializer
)


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
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'ok': True,
                    'token': login_serializer.validated_data.get('access'),
                    'refreshToken': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Login successfull'
                }, status=status.HTTP_200_OK)
            return Response({'ok': False, 'message': 'Email or password wrong'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'ok': False, 'message': 'User does not exist or wrong login info'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        user = User.objects.filter(email=request.data.get('email', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'ok': True, 'message': 'Logout correctly.'}, status=status.HTTP_200_OK)
        return Response({'ok': False, 'message': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    permission_classes = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                .filter(is_active=True)\
                .values('id', 'username', 'email')
        return self.queryset

    def get_permissions(self):
        if self.request.method in ('GET', 'POST'):
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(self.__class__, self).get_permissions()

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        try:
            user = self.get_object(pk)
            password_serializer = PasswordSerializer(data=request.data)

            if password_serializer.is_valid():
                user.set_password(
                    password_serializer.validated_data['password'])
                user.save()
                return Response({
                    'ok': True,
                    'message': 'Password updated.'
                }, status=status.HTTP_200_OK)

            return Response({
                'ok': False,
                'message': 'Information errors.',
                'errors': password_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'ok': False,
                'message': 'Error setting password.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:
            users = self.get_queryset()
            users_serializer = self.list_serializer_class(users, many=True)
            return Response({
                'ok': True,
                'message': 'Users listed correctly.',
                'data': users_serializer.data,
                'total': len(users_serializer.data)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'ok': False,
                'message': 'Error listing users.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            user_serializer = self.serializer_class(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({
                    'ok': True,
                    'message': 'User created correctly.'
                }, status=status.HTTP_201_CREATED)

            return Response({
                'ok': False,
                'message': 'Register errors.',
                'errors': user_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'ok': False,
                'message': 'Error creating user.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            user = self.get_object(pk)
            user_serializer = self.serializer_class(user)

            return Response({
                'ok': True,
                'user': user_serializer.data,
                'message': 'UJser retrived correctly.'},
                status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'ok': False,
                'message': 'Error getting user.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            user = self.get_object(pk)
            user_serializer = UpdateUserSerializer(user, data=request.data)

            if user_serializer.is_valid():
                user_serializer.save()
                return Response({
                    'ok': True,
                    'message': 'User updated.'
                }, status=status.HTTP_200_OK)
            return Response({
                'ok': False,
                'message': 'Updating errors.',
                'errors': user_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'ok': False,
                'message': 'Error updating user.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            user_destroy = self.model.objects.filter(
                id=pk).update(is_active=False)

            if user_destroy == 1:
                return Response({
                    'ok': True,
                    'message': 'User deleted.'
                }, status=status.HTTP_200_OK)

            return Response({
                'ok': False,
                'message': 'User not found.'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'ok': False,
                'message': 'Error deleting user.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
