# login.urls.py
from django.urls import path
from .views import manager_index,manager_log,manager_situation_edit,manager_student_management,manager_teacher_management


urlpatterns = [
    path('', manager_index, name='student_home'),
    path('log/', manager_log, name='student_log'),
    path('situation_edit/', manager_situation_edit, name='situation_edit'),
    path('student_management/', manager_student_management, name='student_management'),
    path('teacher_management/', manager_teacher_management, name='teacher_management'),
]