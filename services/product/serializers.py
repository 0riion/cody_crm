from rest_framework import serializers
from .models import Product
from services.category.serializers import CategoryRetrieveSerializer
from services.price.serializers import PriceRetrieveSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryRetrieveSerializer(many=True)
    price = PriceRetrieveSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'price',
            'category',
        )


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryRetrieveSerializer(many=True)
    price = PriceRetrieveSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'product_description',
            'category',
            'price',
            'created_at',
            'updated_at',
            'is_active',
        )
