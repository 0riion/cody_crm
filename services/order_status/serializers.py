from rest_framework import serializers
from .models import OrderStatus


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = (
            'id',
            'order_status',
        )


class OrderStatusRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = (
            'id',
            'order_status',
            'created_at',
            'updated_at',
            'is_active',
        )
