# myapp/templatetags/get_item.py
from django import template

register = template.Library()

@register.filter
def get_item(entries, date):
    # entriesはCalendarのエントリのリスト、dateは日付
    return next((entry for entry in entries if entry.date == date), None)
