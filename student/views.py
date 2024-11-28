# student/views.py
from django.utils import timezone
from .forms import AttendanceForm,AttendanceReasonForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendance
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
@login_required
def student_home(request):
    current_date = timezone.now().date().isoformat()  # 現在の日付を取得
    current_time = timezone.now().strftime("%H:%M:%S")  # 現在の時刻を「時:分:秒」形式で取得

    if request.method == 'POST':
        print('1')
        form = AttendanceForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            existing_attendance = Attendance.objects.filter(
                date=current_date,  # 出席日が現在の日付と一致するか
                student=request.user,
            ).exists()

            if existing_attendance:
                print('3')
                form.add_error(None, 'すでに出席が登録されています。')
            else:
                print('4')
                attendance = form.save(commit=False)
                attendance.student = request.user
                attendance.attendance_time = timezone.now().time()  # 出席時間を設定
                attendance.reason = None
                attendance.save()
                date = "Calendar object (" + current_date + ")"
                print(form.cleaned_data['date'])
                return redirect('student_home')
        else:
            print('aaa')
            print(form.errors)  # エラー内容を確認
    else:
        print('bbb')
        form = AttendanceForm()

    return render(request, 'student/index.html', {
        'form': form,
        'current_date': current_date,  # 現在の日付をテンプレートに渡す
        'current_time': current_time,  # 現在の時間をテンプレートに渡す
    })


def attendance_list(request):
    # 今日の日付を取得
    today = datetime.today()
    
    # 1ヶ月前の日付を計算
    one_month_ago = today - timedelta(days=30)
    
    # 欠席、遅刻、早退の出席記録のみ、かつ、過去1ヶ月分のデータをフィルタ
    attendance_records = Attendance.objects.filter(
        status__in=['absent', 'late', 'leave_early'],
        date__date__gte=one_month_ago.date()  # 'date' フィールドが1ヶ月前以上の日付
    )

    # 出席記録がない場合のメッセージ
    if not attendance_records.exists():
        message = "未入力はありません"
    else:
        message = None

    return render(request, 'student/attendance_list.html', {
        'attendance_records': attendance_records,
        'message': message,
    })


def input_reason(request, attendance_id):
    # 出席IDに基づいて出席記録を取得
    attendance = get_object_or_404(Attendance, pk=attendance_id)

    if request.method == 'POST':
        form = AttendanceReasonForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()  # 理由を保存
            return redirect('attendance_list')  # 一覧ページにリダイレクト
    else:
        form = AttendanceReasonForm(instance=attendance)

    return render(request, 'student/input_reason.html', {
        'form': form,
        'attendance': attendance,
    })


def student_logout(request):
    return render(request, 'student/logout.html')