# login.urls.py
from django.urls import path
from .views import login

urlpatterns = [
    path('',login , name='index'),
]
