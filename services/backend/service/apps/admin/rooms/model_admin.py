from django.contrib import admin

from .inlines import RentInlines


class RoomModelAdmin(admin.ModelAdmin):
    inlines = [
        RentInlines,
    ]

    list_display = (
        '__str__',
    )

    search_fields = (
        'name',
    )

    readonly_fields = (
        'updated_at',
    )
