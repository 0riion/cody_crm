from rest_framework import serializers
from .models import Customer
from services.address.serializers import AddressSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'identification',
            'first_name',
            'last_name',
            'email',
            'phone',
        )


class CustomerRetrieveSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = (
            'id',
            'identification',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'created_at',
            'updated_at',
            'is_active',
        )
