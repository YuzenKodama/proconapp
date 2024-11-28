# student/views.py
from django.shortcuts import render, get_object_or_404, redirect
from date.models import Calendar
from django.utils import timezone
from django.contrib import messages
import calendar
from datetime import datetime, timedelta



def teacher_home(request):
    now = datetime.now()
    year = now.year
    month = now.month
    # 最新の年月のカレンダー一覧ページにリダイレクト
    return redirect('teacher:teacher_home', year=year, month=month)

def teacher_changepass(request):
    return render(request, 'teacher/changepass.html')

def teacher_edit(request):
    return render(request, 'teacher/edit.html')

def calendar_list(request, year, month):
    # 前月・次月の計算
    if month == 1:
        prev_year = year - 1
        prev_month = 12
    else:
        prev_year = year
        prev_month = month - 1

    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1

    # 月初と月末を計算
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year, month, 31)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)

    # カレンダーに必要な日付を全て取得
    calendars = Calendar.objects.filter(date__range=[start_date.date(), end_date.date()])

    # 月ごとに並べるために日付を7日ごとにグループ化
    calendar_days = []
    week = []
    for calendar in calendars:
        week.append(calendar)
        if len(week) == 7:
            calendar_days.append(week)
            week = []
    if week:  # 最後に7日未満の週があれば、それを追加
        calendar_days.append(week)

    # POSTリクエストで選択された日付を取得して更新
    if request.method == 'POST':
        selected_dates = request.POST.getlist('dates')  # チェックされた日付のリスト

        # 各日付をチェックして、is_holidayをTrueに設定
        for calendar in calendars:
            if str(calendar.date) in selected_dates:
                calendar.is_holiday = True  # チェックされている場合
            else:
                calendar.is_holiday = False  # チェックされていない場合
            calendar.save()

        # 更新後、カレンダー画面にリダイレクト
        return redirect('teacher:calendar_list', year=year, month=month)

    # ビューに渡すデータ
    return render(request, 'teacher/holiday.html', {
        'year': year,
        'month': month,
        'calendar_days': calendar_days,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    })



def teacher_logout(request):
    return render(request, 'teacher/logout.html')
