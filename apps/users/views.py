from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
# Create your views here.

from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None
