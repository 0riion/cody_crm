from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserListSerializer, UserSerializer, UserRetrieveSerializer


class UserView(viewsets.GenericViewSet):
    model = User
    queryset = None
    permission_classes = None

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
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error message: ', e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            queryset = self.get_queryset().filter(
                is_active=True,
                deleted_at=None,
                pk=pk
            )
            serializer = UserRetrieveSerializer(queryset, many=True)
            return Response(serializer.data[0], status=status.HTTP_200_OK)
        except Exception as e:
            print('Error message: ', e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:

            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error message: ', e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.model, pk=pk)
            serializer = UserSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error message: ', e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.model, pk=pk)
            serializer = UserSerializer(
                queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error message: ', e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.model, pk=pk)
            queryset.is_active = False
            queryset.deleted_at = timezone.now()
            queryset.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print('Error message: ', e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
