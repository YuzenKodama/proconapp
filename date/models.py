from django.db import models
import datetime
from django.utils import timezone


class Calendar(models.Model):
    date = models.DateField(unique=True, primary_key=True)  # 日付
    start_time = models.TimeField('開始時間', default=datetime.time(9, 15, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(15, 10, 0))
    is_holiday = models.BooleanField(default=False)  # 休日の有無
    def __str__(self):
        return str(self.date)  # 日付だけを返す