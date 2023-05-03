from django.db import models


class UserStatus(models.TextChoices):
    ADMIN = 'admin'
    USER = 'user'
