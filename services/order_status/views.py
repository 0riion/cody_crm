import uuid
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import OrderStatus
from .serializers import OrderStatusSerializer, OrderStatusListSerializer, OrderStatusRetrieveSerializer
from libs.request_event import camel_to_snake_dict, snake_to_camel_dict


class OrderStatusView(viewsets.GenericViewSet):
    model = OrderStatus
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
            order_status = request.query_params.get('order_status', None)
            created_date_start = request.query_params.get('created_date', None)
            created_date_end = request.query_params.get('created_date', None)

            filter_request = {}
            if order_status:
                filter_request['order_status'] = order_status

            if created_date_start and created_date_end:
                filter_request['created_at__gte'] = created_date_start
                filter_request['created_at__lte'] = created_date_end

            queryset = self.get_queryset().filter(
                is_active=True,
                deleted_at=None,
                **filter_request
            )
            serializer = OrderStatusListSerializer(queryset, many=True)
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
            serializer = OrderStatusRetrieveSerializer(queryset)
            return Response(
                snake_to_camel_dict(serializer.data),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = OrderStatusSerializer(
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
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = OrderStatusSerializer(
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
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = OrderStatusSerializer(
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
            queryset = get_object_or_404(self.get_queryset(), pk=pk)
            queryset.order_status = str(uuid.uuid4()) + '_deleted'
            queryset.description = str(uuid.uuid4()) + '_deleted'
            queryset.deleted_at = timezone.now()
            queryset.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print('Error message: ', e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)
