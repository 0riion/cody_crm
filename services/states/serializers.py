from rest_framework import serializers
from .models import State

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
