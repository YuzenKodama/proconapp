# login.urls.py
from django.urls import path
from .views import login_home, change_pass

urlpatterns = [
    path('', login_home, name='login'),
    path('password/', change_pass , name='change_pass'),
]
