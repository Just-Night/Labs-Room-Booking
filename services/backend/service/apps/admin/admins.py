from apps.admin.site import admin_site
from apps import models

admin_site.register(models.User)
admin_site.register(models.Room)
admin_site.register(models.Rent)
