import uuid
from django.db import models
from services.city.models import City


class Address(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    address = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        null=False,
    )

    zipcode = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        null=False
    )

    city = models.ForeignKey(
        City,
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

    REQUIRED_FIELDS = ['address', 'zipcode', 'city']

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-created_at']
