import uuid

from django.db import models


# Create your models here.
class Warehouse(models.Model):
    """
    Attributes
    ----------
        title: название склада

    """

    title = models.CharField(max_length=255, verbose_name="Название склада")


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
        Warehouse, on_delete=models.CASCADE, verbose_name="название склада"
    )
