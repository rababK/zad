# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm
from .models import Account


class AccountAdmin(UserAdmin):
    form = AccountCreationForm


    list_display = ('email', 'first_name','last_name', 'is_admin','email','password')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'is_admin', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email','is_admin', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'first_name','last_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
