from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, UserPofile
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
    readonly_fields = ["data_joined", "last_seen"]
    list_display = ["username", "phone_number", "email", "is_staff"]
    ordering = ("-id",)
    search_fields = ["phone_number", "username"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "avatar", "birthday", "nick_name"]

admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(UserPofile, UserProfileAdmin)
