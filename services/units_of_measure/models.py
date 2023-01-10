import uuid
from django.db import models


class UnitsOfMeasure(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    unit_name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    case_of_use = models.CharField(
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

    REQUIRED_FIELDS = ['unit_name']

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name = 'Unit of Measure'
        verbose_name_plural = 'Units of Measure'
        ordering = ['unit_name']
