# templatetags/custom_filters.py
from django import template
from date.models import Calendar

register = template.Library()

@register.filter
def get_item(entries, key):
    """
    entries: Calendarのリスト, key: 日付（datetime）
    指定された日付に対応するCalendarエントリを返します。
    """
    return next((entry for entry in entries if entry.date == key), None)
