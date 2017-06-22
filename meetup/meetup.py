import calendar as cal
from datetime import date


def meetup_day(year, month, weekday, des):
    teenth_days = set([13, 14, 15, 16, 17, 18, 19])
    descriptors = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4}
    #descriptors = int(''.join([c for c in '2nd' if c.isdigit()])) - 1
    weekday = list(cal.day_name).index(weekday)

    days = []
    for week in cal.monthcalendar(year, month):
        if week[weekday]:
            days.append(week[weekday])
        
    if des == 'teenth':
        return date(year, month, set(days).intersection(teenth_days).pop())
    if des in descriptors:
        return date(year, month, days[descriptors[des]])
    if des == 'last':
        return date(year, month, days[-1])