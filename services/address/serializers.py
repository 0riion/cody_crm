from rest_framework import serializers
from .models import Address
from services.city.serializers import CityRetrieveSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressListSerializer(serializers.ModelSerializer):
    city = CityRetrieveSerializer(read_only=True)

    class Meta:
        model = Address
        fields = (
            'id',
            'address',
            'zipcode',
            'city',
        )


class AddressRetrieveSerializer(serializers.ModelSerializer):
    city = CityRetrieveSerializer(read_only=True)

    class Meta:
        model = Address
        fields = (
            'id',
            'address',
            'zipcode',
            'city',
            'created_at',
            'updated_at',
            'is_active',
        )
