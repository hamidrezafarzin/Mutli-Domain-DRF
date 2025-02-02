from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("phone",)
    list_filter = ("phone", "is_active", "is_staff", "is_superuser",)
    ordering = ("-created_date",)
    list_display = ("phone", "is_active", "is_staff", "is_superuser",)
    fieldsets = (
        ("Authentication", {"fields": ("phone",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser",)}),
        (
            "Group Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Profile)
