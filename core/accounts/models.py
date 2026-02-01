from django.db import models

# Create your models here.: abstract user model : customise model
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    username=None
    phone_number = models.CharField(max_length=100,unique=True)
    user_bio = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_profile_image = models.ImageField(upload_to='profile')

    #Field Used for login
    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()