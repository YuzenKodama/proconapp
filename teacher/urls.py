# login.urls.py
from django.urls import path
from .views import teacher_home,teacher_base,teacher_holiday,teacher_edit,teacher_changepass,teacher_logout

urlpatterns = [

    path('', teacher_home, name='index'),
    path('base/', teacher_base, name='base'),
    path('edit/', teacher_edit, name='edit'),
    path('holiday/', teacher_holiday, name='holiday'),
    path('changepass/', teacher_changepass, name='changepass'),
    path('logout/', teacher_logout, name='logout'),
]