# login.urls.py
from django.urls import path
from .views import manager_index


urlpatterns = [
    path('', manager_index, name='student_home'),
    path('reason/', student_reason, name='reason'),
    path('changepass/', student_changepass, name='changepass'),
    path('logout/', student_logout, name='logout'),
]