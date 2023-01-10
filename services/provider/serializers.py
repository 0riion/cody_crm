from rest_framework import serializers
from .models import Provider
from services.address.serializers import AddressRetrieveSerializer


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderListSerializer(serializers.ModelSerializer):
    address = AddressRetrieveSerializer(read_only=True)

    class Meta:
        model = Provider
        fields = (
            'id',
            'provider_name',
            'description',
            'email',
            'phone',
            'address',
        )


class ProviderRetrieveSerializer(serializers.ModelSerializer):
    address = AddressRetrieveSerializer(read_only=True)

    class Meta:
        model = Provider
        fields = (
            'id',
            'provider_name',
            'description',
            'email',
            'phone',
            'address',
            'created_at',
            'updated_at',
            'is_active',
        )
