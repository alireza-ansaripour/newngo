__author__ = 'root'
from datetime import datetime
from django import template

register = template.Library()


class Output:
    def __init__(self):
        return


@register.filter(name='jalali')
def persian_date(request):
    date = datetime.now()
    today = datetime(2015, 3, 21)
    days = (date-today).days
    day = 1
    month = 1
    year = 1394

    while days > 0:
        day += 1
        if month <= 6 and day == 32:
            day = 1
            month += 1

        if 6 < month < 12 and day == 31:
            day = 1
            month += 1

        if day == 30 and month == 12:
            if year % 1391 == 0:
                day += 1
            else:
                day = 1
                month = 1
                year += 1

        if day == 31 and month == 12 and year % 1391 ==0:
            day = 1
            month = 1
            year += 1

        days -= 1
    mounths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    weekdays = ['دوشنبه', 'سه شنبه', 'چهار شنبه', 'پنج شنبه', 'جمعه', 'شنبه', 'یکشنبه']

    date3 = datetime(year, month, day)
    output = Output()
    output.day = str(date3.day)
    output.month = mounths[date3.month-1]
    output.year = str(date3.year)
    output.date = str(weekdays[datetime.today().weekday()])+' '+str(date3.day)+' - '+mounths[date3.month-1]+' - '+str(date3.year)+' '
    return output.date


# @register.filter(name='j_day')
class Date:
    def persian_date2(date):
        # date = datetime.now()
        today = date(2015, 3, 21)
        days = (date-today).days
        day = 1
        month = 1
        year = 1394

        while days > 0:
            day += 1
            if month <= 6 and day == 32:
                day = 1
                month += 1

            if 6 < month < 12 and day == 31:
                day = 1
                month += 1

            if day == 30 and month == 12:
                if year % 1391 == 0:
                    day += 1
                else:
                    day = 1
                    month = 1
                    year += 1

            if day == 31 and month == 12 and year % 1391 ==0:
                day = 1
                month = 1
                year += 1

            days -= 1
        mounths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
        weekdays = ['دوشنبه', 'سه شنبه', 'چهار شنبه', 'پنج شنبه', 'جمعه', 'شنبه', 'یکشنبه']

        date3 = datetime(year, month, day)
        output = Output()
        output.day = str(date3.day)
        output.month = mounths[date3.month-1]
        output.year = str(date3.year)
        output.date = str(date3.day)+' - '+mounths[date3.month-1]+' - '+str(date3.year)+' '
        return output.date
