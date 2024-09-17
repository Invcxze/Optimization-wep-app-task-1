from django.urls import path

from .views import get_all_prods

urlpatterns = [
    path("products", get_all_prods),
]
