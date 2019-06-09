from django.contrib.auth.forms import UserCreationForm, forms, UserChangeForm
from .models import *
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'avatar']


class AvatarUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = [ 'username']

    widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            }
