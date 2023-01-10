from rest_framework import serializers
from .models import State

# TODO: Add the cities field to the serializer, to show the cities of the state.


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class StateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            'id',
            'state_name',
        )


class StateRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            'id',
            'state_name',
            'created_at',
            'updated_at',
            'is_active',
        )
