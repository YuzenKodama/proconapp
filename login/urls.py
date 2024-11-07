# login.urls.py
from django.urls import path
from .views import change_pass,login_view,CustomPasswordChangeView,logout_page,CustomLogoutView
from student import views

app_name = 'loginapp'  # ここでapp_nameを設定


urlpatterns = [
    path('', login_view, name='login'),
    path('password/', change_pass , name='change_pass'),
    path('password_change/',CustomPasswordChangeView.as_view(), name='password_change'),
    path('logout/', logout_page, name='logout'),
    path('signout/', CustomLogoutView.as_view(next_page="/login"), name='signout'),
]
