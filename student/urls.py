# login.urls.py
from django.urls import path
from .views import student_home,student_reason,student_logout

urlpatterns = [
    path('', student_home, name='student_home'),
    path('reason/', student_reason, name='reason'),
    path('logout/', student_logout, name='s_logout'),
]