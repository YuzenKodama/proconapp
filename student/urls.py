# login.urls.py
from django.urls import path
from .views import student_home,student_reason,student_changepass,student_logout

urlpatterns = [
    path('', student_home, name='index'),
    path('reason/', student_reason, name='reason'),
    path('changepass/', student_changepass, name='changepass'),
    path('logout/', student_logout, name='logout'),
]