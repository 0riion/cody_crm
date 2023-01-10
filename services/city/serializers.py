from rest_framework import serializers
from .models import City
from services.states.serializers import StateListSerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityListSerializer(serializers.ModelSerializer):
    state = StateListSerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'city_name', 'state')


class CityRetrieveSerializer(serializers.ModelSerializer):
    state = StateListSerializer(read_only=True)

    class Meta:
        model = City
        fields = (
            'id',
            'city_name',
            'state',
            'created_at',
            'updated_at',
            'is_active',
        )
