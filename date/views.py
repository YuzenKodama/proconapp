from django.shortcuts import render
from django.http import HttpResponse
from .utils import initialize_calendar
from datetime import date

def initialize_calendar_view(request):
    start_date = date(2024, 4, 1)
    end_date = date(2025, 3, 31)

    initialize_calendar(start_date, end_date)

    return HttpResponse("カレンダーを初期化しました。")
