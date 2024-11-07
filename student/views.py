# student/views.py
from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import AttendanceForm

from django.contrib.auth.decorators import login_required

#@login_required
def student_home(request):
    current_date = timezone.now().date().isoformat()  # YYYY-MM-DD形式に変換
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = request.user
            attendance.attendance_time = timezone.now().time()
            attendance.reason = None
            attendance.save()
            return redirect('student_home')
    else:
        form = AttendanceForm()

    return render(request, 'student/index.html', {
        'form': form,
        'current_date': current_date,  # 現在の日付をテンプレートに渡す
    })

def student_reason(request):
    return render(request, 'student/reason.html')

def student_logout(request):
    return render(request, 'student/logout.html')