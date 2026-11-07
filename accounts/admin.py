from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class FarnamaUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Student info", {"fields": ("student_number",)}),
    )
    list_display = ("username", "student_number", "is_staff")
