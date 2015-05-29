from datetime import datetime, date

from django.utils import timezone


def datetime_midnight(year, month, day):
    """
    Returns a timezone aware datetime object of a date at midnight, using the
    current timezone.
    """

    return timezone.make_aware(datetime(year, month, day), timezone.get_current_timezone())


def datetime_midnight_date(date_obj):
    """
    Returns a timezone aware datetime object of a date at midnight, using the
    current timezone.
    """

    return datetime_midnight(date_obj.year, date_obj.month, date_obj.day)


def datetime_midnight_today():
    """
    Returns today at midnight as a timezone aware datetime object, using the
    current timezone.
    """

    today = date.today()
    return datetime_midnight(today.year, today.month, today.day)
