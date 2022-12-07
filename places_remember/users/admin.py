from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Display CustomUser model in admin
    """
    model = CustomUser
    list_display = ['email', 'username', 'first_name']
