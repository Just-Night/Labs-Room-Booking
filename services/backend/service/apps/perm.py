from rest_framework.permissions import BasePermission
from apps.user.choices import UserStatus


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.userStatus == UserStatus.ADMIN
