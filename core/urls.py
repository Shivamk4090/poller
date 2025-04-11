from django.urls import  path
from .views import Login, Logout 

urlpatterns = [
    path("login/", Login.as_view(), name='custom_login'),
    path("logout/", Logout.as_view())
]