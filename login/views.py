# login/views.py
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser

def login_home(request):
    return render(request, 'login/login.html')

def change_pass(request):
    return render(request, 'login/Password.html')

def login_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        
        # ユーザー認証
        user = authenticate(request, username=student_id, password=password)
        if user is not None:
            login(request, user)

            # 役割に応じたリダイレクト
            if user.role == CustomUser.Role.STUDENT:
                return redirect('student_view')  # 生徒のビューにリダイレクト
            elif user.role == CustomUser.Role.TEACHER:
                return redirect('teacher_view')  # 先生のビューにリダイレクト
            elif user.role == CustomUser.Role.ADMIN:
                return redirect('admin_view')  # 管理者のビューにリダイレクト
        else:
            messages.error(request, "学生番号またはパスワードが無効です。")
    
    return render(request, 'login.html')  # GETリクエストの場合の処理
