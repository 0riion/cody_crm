from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from services.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
        default=uuid.uuid4
    )

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    username = models.CharField(
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        'Email',
        max_length=255,
        unique=True,
    )

    avatar = models.ImageField(
        'Avatar',
        upload_to='users/avatars',
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

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
