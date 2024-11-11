import uuid

from django.db import models


class Warehouse(models.Model):
    """
    Attributes
    ----------
        title: название склада
        is_remote: удаленный склад или нет

    """

    title = models.CharField(max_length=255, verbose_name="Название склада")
    is_remote = models.BooleanField(
        default=False, verbose_name="Удаленный склад?"
    )

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Product(models.Model):
    """
    Attributes
    ----------
        name: название продукта
        code: код продукта
        warehouse: склад продукта

    """

    name = models.CharField(max_length=255, verbose_name="название продукта")
    code = models.UUIDField(
        unique=True,
        verbose_name="код продукта",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    warehouse = models.ForeignKey(
        Warehouse,
        related_name="products",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Продукт со склада"
        verbose_name_plural = "Продукты со склада"
