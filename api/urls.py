from django.urls import path

from .views import (
    get_all_products,
    get_products_by_group,
    get_products_by_warehouse,
    get_products_by_code,
)

urlpatterns = [
    path("products/", get_all_products),
    path("products/group/<int:pk>/", get_products_by_group),
    path("products/warehouse/", get_products_by_warehouse),
    path("products/code/", get_products_by_code),
]
