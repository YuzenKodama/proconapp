# login.urls.py
from django.urls import path
from .views import login_home, change_pass,login_view
from student import views

urlpatterns = [
    path('', login_view, name='login'),
    path('password/', change_pass , name='change_pass'),
]
