from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from .forms import *
from django.views.decorators.csrf import csrf_protect
from .forms import *

def a(request):
    a = 'Andriy'
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'eshop/index.html', context={'a':a, 'num_visits':num_visits})

def signin(request):
    return render(request, 'eshop/sign-in.html')


class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = "/login/"
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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("eshop/")

def b(request):
    return redirect('base_url')
