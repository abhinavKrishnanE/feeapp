from django.contrib import admin
from .models import CustomUser, UserRole, Permission


admin.site.register(CustomUser)
admin.site.register(UserRole)
admin.site.register(Permission)

