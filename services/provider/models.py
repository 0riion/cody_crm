import uuid
from django.db import models
from services.address.models import Address


class Provider(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    provider_name = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        null=False
    )

    description = models.TextField(
        max_length=255,
        unique=False,
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    phone = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    address = models.ManyToManyField(
        Address,
        related_name='provider_address',
        blank=False,
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

    REQUIRED_FIELDS = ['provider_name', 'email', 'phone', 'address']

    def __str__(self):
        return self.provider_name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
        ordering = ['provider_name']
