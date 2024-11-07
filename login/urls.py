# login.urls.py
from django.urls import path
from .views import login_home, change_pass,login_view,CustomPasswordChangeView
from student import views

app_name = 'loginapp'  # ここでapp_nameを設定


urlpatterns = [
    path('', login_view, name='login'),
    path('password/', change_pass , name='change_pass'),
    path('password_change/',CustomPasswordChangeView.as_view(), name='password_change'),
]
