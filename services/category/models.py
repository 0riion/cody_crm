import uuid
from django.db import models


class Category(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    category_name = models.CharField(
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

    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=False
    )

    REQUIRED_FIELDS = ['category_name']

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']
