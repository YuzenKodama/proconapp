# student/views.py
from django.utils import timezone
from .forms import AttendanceForm,AttendanceReasonForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendance
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from date.models import Calendar

@login_required
def student_home(request):
    current_date = timezone.now().date()  # 現在の日付を取得
    current_time = timezone.now().strftime("%H:%M:%S")  # 現在の時刻を「時:分:秒」形式で取得

    # 今日が休日かどうかをチェック
    try:
        calendar_entry = Calendar.objects.get(date=current_date)
        if calendar_entry.is_holiday:
            # 休日の場合はエラーメッセージを表示
            return render(request, 'student/index.html', {
                'error_message': '今日は休日のため、出席登録はできません。',
                'current_date': current_date,
                'current_time': current_time,
            })
    except Calendar.DoesNotExist:
        pass

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            existing_attendance = Attendance.objects.filter(
                date=current_date,  # 出席日が現在の日付と一致するか
                student=request.user,
            ).exists()

            if existing_attendance:
                # 既に出席登録がある場合はエラーメッセージを表示
                return render(request, 'student/index.html', {
                    'message': '既に出席登録されています。',
                    'current_date': current_date,
                    'current_time': current_time,
                })
            else:
                # 出席登録を保存
                attendance = form.save(commit=False)
                attendance.student = request.user
                attendance.date = current_date
                attendance.save()
                return redirect('student:list')

    else:
        form = AttendanceForm()

    return render(request, 'student/index.html', {
        'form': form,
        'current_date': current_date,
        'current_time': current_time,
    })

@login_required
def list(request):
    # 現在ログインしているユーザーを取得
    user = request.user
    print(user)
    
    # 現在ログインしているユーザーのstudent_idを取得
    student_id = user.student_id
    # student_idが一致する出席データを取得
    attendances = Attendance.objects.filter(student=user)  # 学生に関連する出席データを取得

    # 出席データをテンプレートに渡す
    return render(request, 'student/list.html', {'attendances': attendances})


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