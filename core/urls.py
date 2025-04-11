from django.urls import  path
from .views import Login, Logout, SignUp

urlpatterns = [
    path("login/", Login.as_view(), name='sign_in'),
    path("signUp/", SignUp.as_view(), name='sign_up'),
    path("logout/", Logout.as_view(), name='sign_out')
]