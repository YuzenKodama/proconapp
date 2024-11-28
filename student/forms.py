from django import forms
from .models import Attendance
from django.utils import timezone
from datetime import date



class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'status','attendance_time','reason']  # 日付とステータスをフィールドに含める
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # date フィールドに今日の日付を設定
        self.fields['date'].initial = date.today() # 現在の日付をセット
        self.fields['date'].widget = forms.HiddenInput()


class AttendanceReasonForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['reason']  # 欠席、遅刻、早退の理由フィールド
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

