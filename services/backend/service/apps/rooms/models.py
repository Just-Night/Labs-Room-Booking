from django.db import models
from libs.db.models import BaseModel


class Room(BaseModel):
    name = models.CharField(max_length=50)
    numOfSeats = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} | {self.numOfSeats} | {len(self.rents.all())}'


class Rent(BaseModel):
    room = models.ForeignKey('apps.Room', on_delete=models.CASCADE, related_name='rents')
    user = models.ForeignKey('apps.User', on_delete=models.CASCADE, related_name='rents')
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
