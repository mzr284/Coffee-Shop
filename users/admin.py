from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from django.utils.translation import gettext_lazy as _

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (_("Necessery Informations"), {"fields": ("username", "phone_number")}),
        (_("Personal Informations"), {"fields": ("full_name", "email")}),
        (_("Permission Informations"), {"fields": ("is_active", "is_staff")}),
        (_("Important Date Informations"), {"fields": ("data_joined", "last_seen")}),
    )
    add_fieldsets = (
        ("Create User", {"classes": ("wide",),
                "fields": ("username", "phone_number", "email", "password1", "password2", "is_staff"),}),
    )
    list_display = ["username", "phone_number", "email", "is_staff"]
    ordering = ("-id",)
    search_fields = ["phone_number", "username"]

admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)