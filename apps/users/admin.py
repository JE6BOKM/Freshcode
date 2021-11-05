from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": ("role",),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "role",
    )
