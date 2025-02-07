from django import forms
from date.models import Calendar

class CalendarForm(forms.Form):
    dates = forms.ModelMultipleChoiceField(
        queryset=Calendar.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    is_holiday = forms.BooleanField(required=True, label="一括で休日フラグを変更する", initial=True)