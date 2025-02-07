# login.urls.py
from django.urls import path
from .views import student_home,student_logout,attendance_list,input_reason,list

urlpatterns = [
    path('', student_home, name='student_home'),
    path('logout/', student_logout, name='s_logout'),
    path('attendance_list', attendance_list, name='attendance_list'),  # 出席一覧ページ
    path('list', list, name='list'),  # 出席一覧ページ
    path('input_reason/<int:attendance_id>/', input_reason, name='input_reason'),  # 理由入力ページ
]