from .views import *
from django.urls import path


urlpatterns = [
    path('', a, name='base_url'),
    path('sign-in/', signin, name='sign_in_url'),
    path('register/', RegisterFormView.as_view(), name='register_url'),
    path('login/', LoginFormView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
]
