
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm()
    list_display = ('email', 'is_superuser', 'is_active', 'is_staff')
    list_filter = ('email', 'is_superuser', 'is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('created_date', 'updated_date', 'last_login')
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
        ('Group permissions', {'fields': ('groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_date', 'updated_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )}
        ),
    )
admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)

