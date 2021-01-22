from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
class CustomUserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name, password =None ,commit = True ):
        if not email:
            raise ValueError(_('your email is requered'))
        if not first_name:
            raise ValueError(_('your first name is requered'))
        if not last_name:
            raise ValueError(_('your last name is requered'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name= last_name)
        user.set_password(password)
        if commit :
            user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):

        if not email:
            raise ValueError(_('your email is requered'))
        email = self.normalize_email(email)
        user = self.create_user(email=email, first_name = first_name, last_name=last_name, password=password,commit = False)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




