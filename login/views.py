# login/views.py
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView


def change_pass(request):
    return render(request, 'login/Password.html')

def login_view(request):
    print("login_view", request)
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        
        # ユーザー認証
        try:
            user = CustomUser.objects.get(student_id=student_id)
        except CustomUser.DoesNotExist:
            messages.error(request, "IDが無効です。")
            return render(request, 'login/login.html')  # GETリクエストの場合の処理
            
        if user.password == password:
            login(request, user)

            # 役割に応じたリダイレクト
            if user.role == CustomUser.Role.STUDENT:
                return redirect('student_home')  # 生徒のビューにリダイレクト
            elif user.role == CustomUser.Role.TEACHER:
                return redirect('teacher:teacher_home')  # 先生のビューにリダイレクト
            elif user.role == CustomUser.Role.ADMIN:
                return redirect('manager:manager_home')  # 管理者のビューにリダイレクト
        else:
            messages.error(request, "パスワードが無効です。")
    
    return render(request, 'login/login.html')  # GETリクエストの場合の処理


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'login/change_pass.html'
    success_url = reverse_lazy('password_change_done')  # 変更後のリダイレクト先

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        messages.info(request, "ログアウトしました。")
        logout(request)
        return super().get(request, *args, **kwargs)


def logout_page(request):
    user = request.user
    if user.role == '0':
        base_template = 'student/base.html'
    elif user.role == '1':
        base_template = 'teacher/base.html'
    else:
        base_template = 'login/base.html'  # デフォルトのベーステンプレート

    print(base_template)
    print(user.role)

    return render(request, 'login/logout.html', {'base_template': base_template})