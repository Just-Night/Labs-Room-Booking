from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from apps.perm import IsAdmin
from apps.models import Room, Rent
from apps.rooms import serializers


class CreateRoomAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = serializers.RoomSerializers
    queryset = Room.objects.all()


class ListRoomAPIView(generics.ListAPIView):
    serializer_class = serializers.RoomSerializers
    queryset = Room.objects.all()


class GetRoomAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.RoomSerializers
    queryset = Room.objects.all()


class UpdateRoomAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = serializers.RoomSerializers
    queryset = Room.objects.all()


class DestroyRoomAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = serializers.RoomSerializers
    queryset = Room.objects.all()


class RoomRentsAPIView(generics.ListAPIView):
    serializer_class = serializers.RentSerializers

    def get_queryset(self):
        return Rent.objects.filter(room_id=self.kwargs.get('pk'))


class RentCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.RentCreateSerializers

    def get_object(self):
        return get_object_or_404(
            Room,
            pk=self.kwargs['room']
        )


class RentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.RentCreateSerializers
    queryset = Rent.objects.all().order_by('-created_at')
    lookup_field = 'room'
