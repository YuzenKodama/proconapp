# login.urls.py
from django.urls import path
from .views import manager_home,manager_log,manager_situation_edit,manager_student_management,manager_teacher_management,manager_student_add,manager_teacher_add

app_name = 'manager'  # app_nameを明示的に指定

urlpatterns = [
    path('', manager_home, name='manager_home'),
    path('log/', manager_log, name='log'),
    path('situation_edit/', manager_situation_edit, name='situation_edit'),
    path('student_management/', manager_student_management, name='student_management'),
    path('student_add/', manager_student_add, name='student_add'),
    path('teacher_management/', manager_teacher_management, name='teacher_management'),
    path('teacher_add/', manager_teacher_add, name='teacher_add'),
]