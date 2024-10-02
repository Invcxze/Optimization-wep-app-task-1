from rest_framework import serializers

from .models import Product, Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    """Сериализатор модели склада"""
    class Meta:
        model = Warehouse
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продуктов"""
    warehouse = WarehouseSerializer()

    class Meta:
        model = Product
        fields = "__all__"
