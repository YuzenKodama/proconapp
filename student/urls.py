# login.urls.py
from django.urls import path
from .views import student_home,student_reason

urlpatterns = [
    path('', student_home, name='index'),
    path('reason/', student_reason, name='reason'),
]
