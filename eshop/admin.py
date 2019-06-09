from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    fields = ['username', 'email', 'password', 'phone_number', 'is_staff', 'is_active']
    list_filter = ['is_staff']
    search_fields = ['username', 'email']

    class Meta:
        model = User

admin.site.register(User, UserAdmin)
