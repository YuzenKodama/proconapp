
from django.urls import path
from .views import admin_home,admin_base,admin_edit,admin_changepass,admin_logout,admin_index

urlpatterns = [

    path('', admin_home, name='index'),
    path('base/', admin_base, name='base'),
    path('edit/', admin_edit, name='edit'),
    path('holiday/', admin_changepass, name='changepass'),
    path('logout/', admin_logout, name='logout'),
]