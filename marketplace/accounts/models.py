from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from PIL import Image

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None,):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must enter a password')    

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_staffuser(self, email, password=None,):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_superuser = models.BooleanField(default=False) # a superuser
    avatar = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstname 

    def get_short_name(self):
        # The user is identified by their email address
        return self.firstname

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="store")
   
    def __str__(self):
        return f'{self.user.get_short_name()} Store'

    