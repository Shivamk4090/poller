from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class Login(LoginView):
    form_class = AuthenticationForm
    template_name =  "auth/login.html"
    redirect_authenticated_user = True
    
    

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name =  "auth/signup.html"
    success_url = reverse_lazy('sign_in')


class Logout(LogoutView):
    pass
