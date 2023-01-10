from rest_framework import serializers
from .models import Order
from services.customer.serializers import CustomerListSerializer
from services.order_status.serializers import OrderStatusRetrieveSerializer
from services.product.serializers import ProductRetrieveSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    customer = CustomerListSerializer()
    order_status = OrderStatusRetrieveSerializer()
    product = ProductRetrieveSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'title',
            'order_info',
            'customer',
            'order_status',
            'product',
        )


class OrderRetrieveSerializer(serializers.ModelSerializer):
    customer = CustomerListSerializer()
    order_status = OrderStatusRetrieveSerializer()
    product = ProductRetrieveSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'title',
            'order_info',
            'customer',
            'order_status',
            'product',
            'created_at',
            'updated_at',
            'is_active',
        )
