import uuid
from django.db import models
from services.address.models import Address


class Warehouse(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    warehouse_name = models.CharField(
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

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
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

    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
        ordering = ['created_at']
