
from django.contrib import admin
from .models import AD , post

from django.contrib.auth.admin import UserAdmin
import datetime


def approve(modeladmin, request, queryset):
    queryset.update(acceptance=1, pub_date=datetime.datetime.now())

approve.short_description = "agree published this ads"


class ADAdmin(admin.ModelAdmin):
    list_display = ['Ad_title','Ad_details','photo',]
    actions = ['approve']



admin.site.register(AD,ADAdmin)

admin.site.register(post)