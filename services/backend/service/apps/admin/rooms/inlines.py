from django.contrib import admin

from apps.models import Rent


class RentInlines(admin.TabularInline):
    model = Rent

    fields = (
        'room',
        'user',
        'time_start',
        'time_end',
    )

    autocomplete_fields = (
        'room',
        'user',
    )
