# student/views.py
from django.shortcuts import render, get_object_or_404, redirect
from date.models import Calendar
from django.utils import timezone
from django.contrib import messages
import calendar

def teacher_base(request):
    return render(request, 'teacher/base.html')

def teacher_home(request):
    return render(request, 'teacher/index.html')

def teacher_changepass(request):
    return render(request, 'teacher/changepass.html')

def teacher_edit(request):
    return render(request, 'teacher/edit.html')



from django.shortcuts import render
from datetime import datetime, timedelta

# 月ごとのカレンダーを表示
def calendar_list(request, year, month):
    # 月初と月末を計算
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) - timedelta(days=1) if month < 12 else datetime(year, month, 31)

    # カレンダーに必要な日付を全て取得
    calendars = Calendar.objects.filter(date__range=[start_date.date(), end_date.date()])

    # 月ごとに並べるために日付を7日ごとにグループ化
    calendar_days = []
    week = []
    for calendar in calendars:
        # 一週間の枠に日付を追加
        week.append(calendar)
        if len(week) == 7:
            calendar_days.append(week)
            week = []
    if week:  # 最後に7日未満の週があれば、それを追加
        calendar_days.append(week)

    # ビューに渡すデータ
    return render(request, 'teacher/holiday.html', {
        'year': year,
        'month': month,
        'calendar_days': calendar_days,
    })

def teacher_logout(request):
    return render(request, 'teacher/logout.html')
