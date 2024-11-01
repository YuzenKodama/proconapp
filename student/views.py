# student/views.py
from django.shortcuts import render,redirect



from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Attendance, Calendar
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required

@login_required
def student_home(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            Attendance = form.save(commit=False)
            Attendance.student = request.user  # 現在のユーザーを取得
            Attendance.attendance_time = timezone.now().time()  # 現在の時間を設定
            Attendance.reason = None  # 理由はnullで設定
            Attendance.save()
            return redirect('student_home')  # 登録成功後のリダイレクト先を適宜変更
    else:
        form = AttendanceForm()

    # カレンダーから日付を選ぶための情報を取得
    calendar_dates = Calendar.objects.all()

    return render(request, 'student/index.html', {
        'form': form,
        'calendar_dates': calendar_dates,
    })


def student_reason(request):
    return render(request, 'student/reason.html')

def student_changepass(request):
    return render(request, 'student/changepass.html')

def student_logout(request):
    return render(request, 'student/logout.html')