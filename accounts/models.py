from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager
from django.utils import timezone


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    special_user = models.DateTimeField(default=timezone.now)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin