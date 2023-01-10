import uuid
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer, ProductRetrieveSerializer
from libs.request_event import camel_to_snake_dict, snake_to_camel_dict


class ProductView(viewsets.GenericViewSet):
    model = Product
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
            product_name = request.query_params.get('product_name', None)
            created_date_start = request.query_params.get('created_date', None)
            created_date_end = request.query_params.get('created_date', None)

            filter_request = {}
            if product_name:
                filter_request['product_name__icontains'] = product_name

            if created_date_start and created_date_end:
                filter_request['created_at__gte'] = created_date_start
                filter_request['created_at__lte'] = created_date_end

            queryset = self.get_queryset().filter(
                is_active=True,
                deleted_at=None,
                **filter_request
            )
            serializer = ProductListSerializer(queryset, many=True)
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
            serializer = ProductRetrieveSerializer(queryset)
            return Response(
                snake_to_camel_dict(serializer.data),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            data = camel_to_snake_dict(request.data)
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            data = camel_to_snake_dict(request.data)
            serializer = ProductSerializer(queryset, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            data = camel_to_snake_dict(request.data)
            serializer = ProductSerializer(queryset, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    snake_to_camel_dict(serializer.data),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            queryset.product_name = str(uuid.uuid4()) + '_deleted'
            queryset.product_description = str(uuid.uuid4()) + '_deleted'
            queryset.is_active = False
            queryset.deleted_at = timezone.now()
            queryset.save()
            return Response(
                {'message': 'Delete successfully'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)
