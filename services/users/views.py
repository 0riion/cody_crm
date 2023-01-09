
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
        if self.request.method in ():
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    def list(self, request):

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

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset().filter(
            is_active=True,
            deleted_at=None,
            pk=pk
        )
        serializer = UserRetrieveSerializer(queryset, many=True)
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = get_object_or_404(self.model, pk=pk)
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
