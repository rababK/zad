from django.db import models

import datetime
from django.utils import timezone

from phone_field import PhoneField, PhoneWidget
# from django.contrib.auth.models import User, get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import CustomUserManager
# Create your models here.
import random
import os
import uuid

def upload_path(instance, filename):
    imagename, extension = filename.split(".")

    return "post/%s.%s" % (instance.id, extension)


# settings.AUTH_USER_MODEL

class AD(models.Model):
    #id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    categories = ((1, 'product'), (2, 'service'), (3, 'course'), (4, 'store'), (5, 'other'))

    Ad_title = models.TextField(verbose_name="ad about:", max_length=50, blank=False, editable=True, null=False,
                                default="null", help_text="TITLE:")
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Ad_details = models.TextField(verbose_name="ad about:", max_length=500, blank=False, editable=True,
                                  help_text="DETAILS:")
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, blank=False,
                                       verbose_name="date of publish  the advertice")
    category = models.IntegerField(choices=categories, blank=False, null=False)

    objects = models.Manager()

    photo = models.ImageField(blank=False, upload_to=upload_path, help_text="PHOTO:")

    def __str__(self):
        return self.Ad_title


class post(models.Model):
    period_choices = ((24, "day"), (48, "tow days"), (72, "three days"))
    AD = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='post', blank=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adder')
    publish_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    period = models.IntegerField(choices=period_choices, blank=False, null=False, help_text="PERIOD")
    approved = models.BooleanField(default=False, blank=True)
    unvalid = models.BooleanField(default=False, blank=True)
    vote = models.IntegerField(blank=True, null=False, help_text="VOTE:", default=0)
    objects = models.Manager()

    def __str__(self):
        return self.AD.Ad_title


class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.CharField(blank=False, max_length=200, help_text='add comment:')

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='User_comments')

    def __str__(self):
        return self.comment_text
