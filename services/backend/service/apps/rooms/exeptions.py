from rest_framework import status
from rest_framework.exceptions import APIException


class RentTimeExeptions(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'This time range is already reserved for this room'
