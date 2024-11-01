import holidays
from django.utils import timezone
from datetime import timedelta
from .models import Calendar

def get_holidays(year):
    return holidays.Japan(years=year)

def is_weekend(date):
    return date.weekday() >= 5  # 土曜日(5)または日曜日(6)

def initialize_calendar(start_date, end_date):
    jp_holidays = get_holidays(start_date.year)
    current_date = start_date

    while current_date <= end_date:
        is_holiday = is_weekend(current_date) or (current_date in jp_holidays)
        Calendar.objects.get_or_create(
            date=current_date,
            defaults={'is_holiday': is_holiday}
        )
        current_date += timedelta(days=1)
