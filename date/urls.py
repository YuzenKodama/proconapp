from django.urls import path
from .views import initialize_calendar_view

urlpatterns = [
    path('', initialize_calendar_view, name='initialize_calendar'),
]
