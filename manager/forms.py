from django import forms
from login.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'student_id', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'ユーザー名',
            'student_id': '学生ID',
            'email': 'メールアドレス',
            'password': 'パスワード',
        }