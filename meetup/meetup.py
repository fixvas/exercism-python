import calendar as cal
from datetime import date


TEENTH_DAYS = set([13, 14, 15, 16, 17, 18, 19])
DESCRIPTORS = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday, des):
    weekday = list(cal.day_name).index(weekday)
    days = []
    for week in cal.monthcalendar(year, month):
        if week[weekday]:
            days.append(week[weekday])
        
    if des == 'teenth':
        return date(year, month, set(days).intersection(TEENTH_DAYS).pop())
    if des in DESCRIPTORS:
        try:
            return date(year, month, days[DESCRIPTORS[des]])
        except IndexError:
            raise MeetupDayException()