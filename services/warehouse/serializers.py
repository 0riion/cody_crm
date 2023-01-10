from rest_framework import serializers
from .models import Warehouse
from services.address.serializers import AddressSerializer

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class WarehouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = (
            'id',
            'warehouse_name',
            'description',
            'address',
            'created_at',
            'updated_at',
            'is_active',
        )

class WarehouseRetrieveSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, read_only=True)

    class Meta:
        model = Warehouse
        fields = (
            'id',
            'warehouse_name',
            'description',
            'address',
            'created_at',
            'updated_at',
            'is_active',
        )

