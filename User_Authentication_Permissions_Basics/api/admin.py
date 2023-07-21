from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class MyUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number',)}),
    )

admin.site.register(CustomUser, MyUserAdmin)
