from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction, models
from apps.user import choices


class UserQuerySet(models.QuerySet):
    ...


class CustomUserManager(BaseUserManager):

    def create_superuser(self, password=None, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        kwargs.setdefault('userStatus', choices.UserStatus.ADMIN)
        return self.create_user(password, **kwargs)

    @transaction.atomic
    def create_user(self, password=None, **kwargs):
        user = self.model(**kwargs)

        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user


UserManager = CustomUserManager.from_queryset(UserQuerySet)
