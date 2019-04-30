from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=12, blank=True, unique=True)
