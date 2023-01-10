import uuid
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Category
from .serializers import CategorySerializer, CategoryListSerializer, CategoryRetrieveSerializer
from libs.request_event import camel_to_snake_dict, snake_to_camel_dict


class CategoryView(viewsets.GenericViewSet):
    model = Category
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
        try:
            category_name = request.query_params.get('category_name', None)
            created_date_start = request.query_params.get('created_date', None)
            created_date_end = request.query_params.get('created_date', None)

            filter_request = {}
            if category_name:
                filter_request['category_name__contains'] = category_name
            if created_date_start and created_date_end:
                filter_request['created_at__gte'] = created_date_start
                filter_request['created_at__lte'] = created_date_end

            queryset = self.get_queryset().filter(
                is_active=True,
                deleted_at=None,
                **filter_request
            )
            serializer = CategoryListSerializer(queryset, many=True)
            return Response(
                [snake_to_camel_dict(item) for item in serializer.data],
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = CategoryRetrieveSerializer(queryset)
            return Response(
                snake_to_camel_dict(serializer.data),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = CategorySerializer(
                data=camel_to_snake_dict(request.data))
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_201_CREATED
                )
            return Response(
                snake_to_camel_dict(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), id=pk)
            serializer = CategorySerializer(
                queryset, data=camel_to_snake_dict(request.data))
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_200_OK
                )
            return Response(
                snake_to_camel_dict(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), id=pk)
            serializer = CategorySerializer(
                queryset, data=camel_to_snake_dict(request.data), partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_200_OK
                )
            return Response(
                snake_to_camel_dict(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), id=pk)
            queryset.category_name += str(uuid.uuid4()) + '_deleted'
            queryset.description = str(uuid.uuid4()) + '_deleted'
            queryset.is_active = False
            queryset.deleted_at = timezone.now()
            queryset.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)
