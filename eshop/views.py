from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView, DeleteView, UpdateView
from django.contrib.auth import logout
from .forms import *
from .models import User



def redirect_to_base_page(request):
    return redirect('base_url')

def base_page(request):
    a = 'Andriy'
    return render(request, 'eshop/index.html', context={'a':a})


class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = "/eshop/login/"
    template_name = "eshop/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "eshop/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def signin(request):
    return render(request, 'eshop/sign-in.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def profile(request, username):
    return render(request, 'eshop/profile.html')

class UserChangeView(UpdateView):
    model = User
    fields = ['avatar']
    template_name_suffix = '_update_form'
    success_url = "/"

    def get_queryset(self):
        return User.objects.all()
