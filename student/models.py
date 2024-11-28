from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from date.models import Calendar

class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('present', '登校'),
        ('absent', '欠席'),
        ('late', '遅刻'),
        ('leave_early', '早退'),
    ]

    attendance_id = models.AutoField(primary_key=True)  # 出席ID
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 生徒
    date = models.ForeignKey(Calendar, on_delete=models.CASCADE)  # 日付（授業日）
    status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS_CHOICES)  # 出席状況
    attendance_time = models.TimeField(null=True, blank=True)  # 登校時間（遅刻の場合は入力）
    reason = models.TextField(null=True, blank=True)  # 欠席、遅刻理由