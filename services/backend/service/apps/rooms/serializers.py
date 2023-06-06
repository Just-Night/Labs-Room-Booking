from rest_framework import serializers
from django.db import transaction
from apps.user import serializers as user_serializers
from apps.models import Rent, Room
from .exeptions import RentTimeExeptions


class RoomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = (
            'uuid',
            'name',
            'numOfSeats'
        )


class RentSerializers(serializers.ModelSerializer):
    room = RoomSerializers(read_only=True)
    user = user_serializers.UserSerializers(read_only=True)

    class Meta:
        model = Rent
        fields = (
            'uuid',
            'user',
            'time_start',
            'time_end',
            'room'
        )


class RentCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = (
            'room',
            'time_start',
            'time_end',
        )

    def validate(self, data):

        rents = Rent.objects.filter(
            room=data.get('room'),
            time_start__lte=data.get('time_start'),
            time_end__gte=data.get('time_end'),
        )
        if rents.exists():
            raise RentTimeExeptions()

        return data

    @transaction.atomic
    def create(self, validated_data):

        room = validated_data.get('room')
        return room.rents.create(
            user=self.context['request'].user,
            time_start=validated_data.get('time_start'),
            time_end=validated_data.get('time_end')
        )
