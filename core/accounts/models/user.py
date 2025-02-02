from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from utils.errors.constants import Errors
from utils.validators import iranian_phone_validator, xss_validator

class UserManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, password=None, **extra_fields):
        """
        Custom user model manager where phone is the unique identifiers
        for authentication instead of usernames.
        """
        if not phone:
            raise ValueError(_("The phone must be set"))
        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)    
        else:
            user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given phone and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(
        _("Phone"),
        max_length=11,
        unique=True,
        validators=[
            iranian_phone_validator,
            xss_validator,
        ],
        blank=False,
        null=False,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = [
            "-id",
        ]

    def __str__(self):
        return f"{self.phone}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)