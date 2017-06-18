from datetime import timedelta


def add_gigasecond(origin_date):
    return origin_date + timedelta(seconds=10**9)
