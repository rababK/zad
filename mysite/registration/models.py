import os
import random
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
# Create your models here.

from django.core.validators import RegexValidator
# new_file_name -> p{user_id}_{file_name_in_user_os}
# use this format to extract file_name in user_os
# new_file_name is needed for unique file_name of our own choice
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
class accountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    #use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True.'))
        return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_created=True, auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    objects = accountManager()

    REQUIRED_FIELDS = ['first_name','last_name','password',]

    def get_full_name(self):
        return "{} {}".format(self.first_name,self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.first_name


def upload_path(instance, filename):
    if instance.picture:
        fileid = instance.user.id
    else:
        random.seed(datetime.now())
        fileid = random.randint(int(1e9), int(1e10))
        print(fileid)
    new_filename = 'p{0}_{1}'.format(fileid, filename)
    path = 'profile_images'
    return os.path.join(path, new_filename)


# no picture uploaded...we have to handle it securely


class UserProfile(models.Model):
    user = models.OneToOneField(Account, unique=True,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=upload_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
