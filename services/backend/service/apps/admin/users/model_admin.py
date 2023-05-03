from django.contrib import admin

from apps.admin.rooms.inlines import RentInlines


class UserModelAdmin(admin.ModelAdmin):
    inlines = [
        RentInlines,
    ]

    list_display = (
        '__str__',
    )

    search_fields = (
        'username',
        'email',
    )

    readonly_fields = (
        'updated_at',
    )
