# login/views.py
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

def login_home(request):
    return render(request, 'login/login.html')

def change_pass(request):
    return render(request, 'login/Password.html')

def login_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        
        # ユーザー認証
        try:
            user = CustomUser.objects.get(student_id=student_id)
        except CustomUser.DoesNotExist:
            messages.error(request, "IDかパスワードが無効です。")
            return render(request, 'login/login.html')  # GETリクエストの場合の処理
            
        if user.password == password:
            login(request, user)

            # 役割に応じたリダイレクト
            if user.role == CustomUser.Role.STUDENT:
                return redirect('student_home')  # 生徒のビューにリダイレクト
            elif user.role == CustomUser.Role.TEACHER:
                return redirect('teacher_home')  # 先生のビューにリダイレクト
            elif user.role == CustomUser.Role.ADMIN:
                return redirect('admin_home')  # 管理者のビューにリダイレクト
        else:
            messages.error(request, "パスワードが無効です。")
    
    return render(request, 'login/login.html')  # GETリクエストの場合の処理


# パスワード変更ビュー
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'login/change_pass.html'  # 使用するテンプレート
    success_url = reverse_lazy('login:login')  # 成功後のリダイレクト先

# パスワード変更完了ページビュー
class PasswordChangeDoneView(TemplateView):
    template_name = 'login/change_pass.html'  # 完了ページのテンプレート
