from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_OPTION = (("C", "Client"),("E", "Engineer"), ("S", "Staff"))
    email = models.EmailField(_('email address'), unique=True, max_length=60)
    first_name = models.CharField(null=True, blank=True, max_length=60)
    last_name = models.CharField(null=True, blank=True, max_length=60)
    address = models.CharField(null=True, blank=True, max_length=250)
    business_name = models.CharField(null=True, blank=True, max_length=200)
    user_status = models.CharField(max_length=22, choices=USER_OPTION, default="Client")
    phone_number = models.CharField(null=True, blank=True, unique=True, max_length=14)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Last login")
    is_password_changed = models.BooleanField(default = False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.email}'
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_staff

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True