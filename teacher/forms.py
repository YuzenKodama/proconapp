from django import forms
from date.models import Calendar

class HolidayFormClass(forms.Form):
    date = forms.DateField()  # 日付
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    is_holiday = forms.BooleanField()  # 休日の有無