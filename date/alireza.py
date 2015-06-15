from datetime import datetime

from Ngo.persons.models import NGO


def say_hello(request):
        return {
            'america': NGO.objects.filter(continent='am'),
            'europe': NGO.objects.filter(continent='er'),
            'africa': NGO.objects.filter(continent='af'),
            'australia': NGO.objects.filter(continent='au'),
            'asia': NGO.objects.filter(continent='as'),
            'say_hello': "Hello",
        }



def persian_date(news):
    day = news.date.day
    month = news.date.month
    year = news.date.year
    date = datetime(year, month, day)

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
    return str(date3.day)+' - '+mounths[date3.month-1]+' - '+str(date3.year)+' '