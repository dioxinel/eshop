from django.contrib.auth.forms import UserCreationForm, forms
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'avatar']


class AvatarUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['avatar']
