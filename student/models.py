from django.db import models
from django.conf import settings  # CustomUserモデルを使用するため
from date.models import Calendar  # Calendarモデルをインポート

class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('present', '出席'),
        ('absent', '欠席'),
        ('late', '遅刻'),
        ('leave_early', '早退'),
        ('school_absence', '校欠'),
    ]

    attendance_id = models.AutoField(primary_key=True)  # 出席ID（主キー）
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # CustomUserモデルから学生番号
    date = models.ForeignKey(Calendar, on_delete=models.CASCADE)  # Calendarモデルから日付
    status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS_CHOICES)  # 出席状況
    attendance_time = models.TimeField(null=True, blank=True)  # 出席時間
    reason = models.TextField(null=True, blank=True)  # 欠席、早退、遅刻理由

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
