import uuid
from django.db import models


class State(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    state_name = models.CharField(
        max_length=255,
        unique=True,
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

    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=False
    )

    REQUIRED_FIELDS = ['state_name']

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        ordering = ['state_name']

