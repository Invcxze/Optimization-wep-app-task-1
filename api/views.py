from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
def get_all_products(request: Request) -> Response:
    """Получение всех продуктов из бд"""
    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products_by_group(request: Request, group_id: int) -> Response:
    """Получение продуктов из бд по группе"""
    products = Product.objects.filter(group=group_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products_by_warehouse(request: Request) -> Response:
    """Получение продуктов из бд в соответствии с удаленным/нашим складом"""
    is_our_warehouse = request.query_params.get("remote")
    products = Product.objects.filter(warehouse__is_remote=is_our_warehouse)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products_by_code(request: Request) -> Response:
    """Получение продуктов из бд по коду"""
    code = request.query_params.get("code")
    products = Product.objects.filter(code=code)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
