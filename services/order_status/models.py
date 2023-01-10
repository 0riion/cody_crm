import uuid
from django.db import models


class OrderStatus(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    order_status = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    description = models.CharField(
        max_length=255,
        unique=False,
        blank=True,
        null=True
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
        return self.order_status

    class Meta:
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'
        ordering = ['order_status']
