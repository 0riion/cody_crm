import uuid
from django.db import models
from services.customer.models import Customer
from services.order_status.models import OrderStatus
from services.product.models import Product


class Order(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    title = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        null=False
    )

    order_info = models.CharField(
        max_length=255,
        unique=False,
        blank=True,
        null=True
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    order_status = models.ForeignKey(
        OrderStatus,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    product = models.ManyToManyField(
        Product,
        blank=False,
        null=False,
        related_name='product'
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

    REQUIRED_FIELDS = ['order_status']

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['created_at']
