
from django.contrib import admin
from .models import AD
from django.utils import timezone
from django.contrib.auth.admin import UserAdmin
import datetime
from django.utils.translation import gettext_lazy as _

def approved(modeladmin, request, queryset):
    for ad in queryset:
        ad.approved=True
        ad.publish_date=timezone.now()
        ad.save()
approved.short_description = "agree published this ads"


class ADAdmin(admin.ModelAdmin):
    list_display = ['Ad_title','Ad_details','photo','term','user','category','approved','valid','created_at','update_at','publish_date','number_of_likes']
    search_fields = ['Ad_title', 'category','user']
    actions = [approved]



admin.site.register(AD,ADAdmin)

