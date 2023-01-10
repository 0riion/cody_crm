from rest_framework import serializers
from .models import Price
from services.units_of_measure.serializers import UnitsOfMeasureRetrieveSerializer


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'unit_of_measure',
            'price',
        )


class PriceRetrieveSerializer(serializers.ModelSerializer):
    unit_of_measure = UnitsOfMeasureRetrieveSerializer()

    class Meta:
        model = Price
        fields = (
            'id',
            'unit_of_measure',
            'price',
            'created_at',
            'updated_at',
            'is_active',
        )
