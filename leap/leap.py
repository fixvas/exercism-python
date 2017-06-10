#!/usr/bin/python3


def is_leap_year(year):
    if (year % 4) != 0:
        return False
    else:
        if (year % 100) != 0:
            return True
        else:
            if (year % 400) == 0:
                return True
            else:
                return False
