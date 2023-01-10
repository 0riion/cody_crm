from rest_framework import serializers
from .models import UnitsOfMeasure


class UnitsOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitsOfMeasure
        fields = '__all__'


class UnitsOfMeasureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitsOfMeasure
        fields = (
            'id',
            'unit_name',
        )


class UnitsOfMeasureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitsOfMeasure
        fields = (
            'id',
            'unit_name',
            'case_of_use',
            'created_at',
            'updated_at',
            'is_active',
        )
