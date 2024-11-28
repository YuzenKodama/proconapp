# login.urls.py
from django.urls import path
from .views import teacher_home,teacher_edit,teacher_changepass,teacher_logout,calendar_list

app_name = 'teacher'  # app_nameを明示的に指定


urlpatterns = [
    path('', teacher_home, name='teacher_home'),
    path('edit/', teacher_edit, name='edit'),
    path('calendar/<int:year>/<int:month>/', calendar_list, name='calendar_list'),
    path('changepass/', teacher_changepass, name='changepass'),
    path('logout/', teacher_logout, name='t_logout'),
]