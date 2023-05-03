from rest_framework import serializers
from django.db import transaction
from apps.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'firstName',
            'lastName',
            'phone',
            'userStatus'
        ]


class RegistrationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'firstName',
            'lastName',
            'phone',
            'password',
        ]

    @transaction.atomic()
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            firstName=validated_data.get('firstName'),
            lastName=validated_data.get('lastName'),
            phone=validated_data.get('phone'),
            password=validated_data.get('password'),
        )
        return user
