from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .actions.timed import length_time
from .models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
@cache_page(60 * 15)
def get_all_products(request: Request) -> Response:
    """Получение всех продуктов из бд"""
    products = Product.objects.select_related("warehouse").all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products_by_group(request: Request, group_id: int) -> Response:
    """Получение продуктов из бд по группе"""
    products = Product.objects.filter(group=group_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@length_time
def get_products_by_warehouse(request: Request) -> Response:
    """Получение продуктов из бд в соответствии с удаленным/нашим складом"""
    is_our_warehouse = request.query_params.get("remote")
    is_id_warehouse = request.query_params.get("id")

    if not is_our_warehouse and not is_id_warehouse:
        return Response(
            {"error": "Пожалуйста, укажите либо 'remote', либо 'id'."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if is_our_warehouse is not None:
        is_our_warehouse = is_our_warehouse.lower() in ["true", "1"]
        products = Product.objects.filter(
            warehouse__is_remote=is_our_warehouse
        )
    else:
        try:
            is_id_warehouse = int(is_id_warehouse)
        except ValueError:
            return Response(
                {"error": "'id' должен быть числом."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        products = Product.objects.filter(warehouse__id=is_id_warehouse)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products_by_code(request: Request) -> Response:
    """Получение продуктов из бд по коду"""
    code = request.query_params.get("code")
    if not code:
        return Response(
            {"error": "Параметр 'code' обязателен."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    products = Product.objects.filter(code=code)
    if not products.exists():
        return Response(
            {"error": "Продукты с таким кодом не найдены."},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
