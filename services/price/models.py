import uuid
from django.db import models
from services.units_of_measure.models import UnitsOfMeasure


class Price(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    unit_of_measure = models.ForeignKey(
        UnitsOfMeasure,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
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

    REQUIRED_FIELDS = ['unit_of_measure', 'price']

    def __str__(self):
        return self.unit_of_measure

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
