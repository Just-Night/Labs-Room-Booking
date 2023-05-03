from apps.admin.site import admin_site
from apps.models import User, Room
from apps.admin.rooms import model_admin as rooms_model
from apps.admin.users import model_admin as users_model

admin_site.register(User, users_model.UserModelAdmin)
admin_site.register(Room, rooms_model.RoomModelAdmin)
