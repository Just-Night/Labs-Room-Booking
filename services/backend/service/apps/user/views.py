from rest_framework import generics, permissions
from django.shortcuts import get_list_or_404
from django.db.models import Q
from apps.models import User, Rent
from apps.user import serializers
from apps.rooms import serializers as rooms_serializers


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializers


class LoginAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserSerializers

    def get_object(self):
        return self.request.user


class FindUserAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserSerializers
    queryset = User.objects.all()
    lookup_field = 'username'


class UserRentsAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = rooms_serializers.RentSerializers

    def get_queryset(self):
        return get_list_or_404(
            Rent,
            Q(user__username=self.kwargs.get('username'))
        )
