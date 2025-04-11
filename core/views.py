from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class Login(LoginView):
    form_class = AuthenticationForm
    template_name =  "auth/login.html"
    redirect_authenticated_user = True


class Logout(LogoutView):
    pass
