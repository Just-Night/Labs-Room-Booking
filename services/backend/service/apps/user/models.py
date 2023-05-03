from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.user import choices, managers
from libs.db.models import BaseModel, NB


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    phone = models.CharField(max_length=15, **NB)
    userStatus = models.CharField(
        max_length=35,
        choices=choices.UserStatus.choices,
        default=choices.UserStatus.USER,
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects: managers.CustomUserManager = managers.UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return f'{self.username} | {self.userStatus}'
