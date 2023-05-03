from rest_framework import serializers
from apps.user import serializers as user_serializers
from apps.models import Rent, Room


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
            'room',
            'user',
            'time_start',
            'time_end',
        )

    def validate(self, data):
        room = data.get('room')
        time_start = data.get('time_start')
        time_end = data.get('time_end')

        rents = Rent.objects.filter(
            room=room,
            time_start__lt=time_end,
            time_end__gt=time_start,
        )

        if rents.exists():
            raise serializers.ValidationError('This time range is already reserved for this room')

        return data


class RentCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = (
            'room',
            'time_start',
            'time_end',
        )

    def validate(self, data):
        room = data.get('room')
        time_start = data.get('time_start')
        time_end = data.get('time_end')

        rents = Rent.objects.filter(
            room=room,
            time_start__lt=time_end,
            time_end__gt=time_start,
        )

        if rents.exists():
            raise serializers.ValidationError('This time range is already reserved for this room')

        return data
