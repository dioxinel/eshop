from django.db import models
from django.contrib.auth.models import *
from django.utils import six, timezone
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, default='User', primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=12, blank=True, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    avatar = models.ImageField(upload_to='media', default='def.png', blank=True)

    def get_profile_url(self):
        return reverse('profile_url', kwargs={'username':self.username})

    def get_avatar_update_url(self):
        return reverse('avatar_update_url', kwargs={'pk':self.username})

    def __str__(self):
        return 'Пользователь %s' % (self.username)
