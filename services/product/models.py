import uuid
from django.db import models
from services.category.models import Category
from services.price.models import Price


class Product(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    product_name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    product_description = models.CharField(
        max_length=255,
        unique=False,
        blank=True,
        null=True
    )

    category = models.ManyToManyField(
        Category,
        blank=True
    )

    price = models.ManyToManyField(
        Price,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        'Created at',
        auto_now_add=True,
        blank=False,
        null=False
    )

    updated_at = models.DateTimeField(
        'Updated at',
        auto_now=True,
        blank=False,
        null=False
    )

    deleted_at = models.DateTimeField(
        'Deleted at',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        blank=False,
        null=False
    )

    REQUIRED_FIELDS = ['product_name', 'category', 'price']

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
