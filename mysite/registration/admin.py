# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AccountCreationForm
from .models import Account


class AccountAdmin(BaseUserAdmin):
    form = AccountCreationForm


    list_display = ('email', 'first_name', 'is_admin','picture')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'is_admin', 'password')}),
        ('Personal info', {'fields': ('name','picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email','is_admin', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
