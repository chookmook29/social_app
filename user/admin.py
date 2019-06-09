from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username']
    fieldsets = (
        (('User'), {'fields': ('username', 'email')}),
        (('Personal'), {'fields': ('first_name', 'last_name', 'image', 'dob')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (('Statuses'), {'fields': ('approved', 'suspended')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
