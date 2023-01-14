import uuid
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from services.users.models import User
from services.users.serializers import (
    UserSerializer,
    UserListSerializer,
    UpdateUserSerializer,
    PasswordSerializer,
    UserRetrieveSerializer
)

from libs.request_event import camel_to_snake_dict, snake_to_camel_dict


class UserViewSet(viewsets.GenericViewSet):
    model = User
    queryset = None
    permission_classes = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects
        return self.queryset

    def get_permissions(self):
        if self.request.method in ('POST'):
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

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
            email = request.query_params.get('email', None)
            user_name = request.query_params.get('user_name', None)
            created_date_start = request.query_params.get('created_date', None)
            created_date_end = request.query_params.get('created_date', None)

            filter_request = {}
            if user_name:
                filter_request['username'] = user_name

            if email:
                filter_request['email'] = email

            if created_date_start and created_date_end:
                filter_request['created_at__gte'] = created_date_start
                filter_request['created_at__lte'] = created_date_end

            queryset = self.get_queryset().filter(
                is_active=True,
                deleted_at=None,
                **filter_request
            )
            serializer = UserListSerializer(queryset, many=True)
            return Response(
                [snake_to_camel_dict(item) for item in serializer.data],
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.model, pk=pk)
            serializer = UserRetrieveSerializer(queryset)
            return Response(
                snake_to_camel_dict(serializer.data),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            body = camel_to_snake_dict(request.data)
            serializer = UserSerializer(data=body)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            user = get_object_or_404(self.model, pk=pk)
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

    def partial_update(self, request, pk=None):
        try:
            user = get_object_or_404(self.model, pk=pk)
            user_serializer = UpdateUserSerializer(
                user, data=request.data, partial=True)

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
            queryset = get_object_or_404(self.model, pk=pk)
            queryset.username += str(uuid.uuid4()) + '_deleted'
            queryset.email += str(uuid.uuid4()) + '_deleted'
            queryset.is_active = False
            queryset.deleted_at = timezone.now()
            queryset.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)
