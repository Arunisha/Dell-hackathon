from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreation,CustomUserChange


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreation
	form = CustomUserChange
	model = CustomUser
	list_display = ['username','email','first_name','last_name','score']


admin.site.register(CustomUser,CustomUserAdmin)


