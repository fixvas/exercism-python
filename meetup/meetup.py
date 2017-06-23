from calendar import monthcalendar
from datetime import date


TEENTH_DAYS = set([13, 14, 15, 16, 17, 18, 19])
DESCRIPTORS = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}
WEEKDAYS = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday':3,
            'Friday':4, 'Saturday':5, 'Sunday':6}


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday, des):
    weekday = WEEKDAYS[weekday]
    
    days = [week[weekday] for week in monthcalendar(year, month) \
            if week[weekday]]
        
    if des == 'teenth':
        return date(year, month, set(days).intersection(TEENTH_DAYS).pop())
    else:
        try:
            return date(year, month, days[DESCRIPTORS[des]])
        except IndexError:
            raise MeetupDayException()