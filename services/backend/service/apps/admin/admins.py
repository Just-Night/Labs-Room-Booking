from apps.admin.site import admin_site
from apps.models import User, Room
from apps.admin.rooms import model_admin as rooms_model


admin_site.register(User)
admin_site.register(Room, rooms_model.RoomModelAdmin)
