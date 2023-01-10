import uuid
from django.db import models
from services.address.models import Address


class Customer(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )
    # TODO: add optional fields and create a service fot identification types
    identification = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        null=False
    )

    last_name = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        null=False
    )

    email = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    address = models.ManyToManyField(
        Address,
        blank=True,
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
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
