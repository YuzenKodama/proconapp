from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from login.models import CustomUser
from student.models import Attendance
from django.utils import timezone
# Create your views here.
@login_required
def manager_home(request):
    attendances = Attendance.objects.all()  # 学生に関連する出席データを取得
    # 出席データとyear、monthをテンプレートに渡す
    return render(request, 'manager/index.html', {
        'attendances': attendances
    })

def manager_log(request):
    return render(request, 'manager/log.html')

def manager_situation_edit(request):
    return render(request, 'manager/situation_edit.html')

def manager_student_management(request):
    # roleがstudentのユーザーを取得
    students = CustomUser.objects.filter(role=CustomUser.Role.STUDENT)
    
    # ユーザーデータをテンプレートに渡す
    return render(request, 'manager/student_management.html', {'students': students})

@login_required
def manager_student_add(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = CustomUser.Role.STUDENT  # ロールの初期値をstudentに設定
            user.save()
            return redirect('manager:student_management')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'manager/student_add.html', {'form': form})

def manager_teacher_management(request):
    # roleがteacherのユーザーを取得
    teachers = CustomUser.objects.filter(role=CustomUser.Role.TEACHER)
    
    # ユーザーデータをテンプレートに渡す
    return render(request, 'manager/teacher_management.html', {'teachers': teachers})

@login_required
def manager_teacher_add(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = CustomUser.Role.TEACHER  # ロールの初期値をteacherに設定
            user.save()
            messages.success(request, '新しい教師が追加されました。')
            return redirect('manager:teacher_management')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'manager/teacher_add.html', {'form': form})