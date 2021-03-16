from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('loginCredentials',loginCredentials),
    path('Logout',Logout),
    path('signUp',signUp),
    path('signUpCredentials',signUpCredentials),   
]
