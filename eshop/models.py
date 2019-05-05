from django.db import models
from django.contrib.auth.models import *
from django.utils import six, timezone
from django.shortcuts import reverse

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, default='User')
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=12, blank=True, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)

    def get_profile_url(self):
        return reverse('profile_url', kwargs={'username':self.username})
