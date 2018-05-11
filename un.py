#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

MONTH_OF_DAYS = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}

MONTH_OF_DAYS_LEAP = {
    "1": 31,
    "2": 29,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}



YEAR_OF_SECONDS = 365 * 24 * 60 * 60
LEAP_YEAR_OF_SECONDS = 366 * 24 * 60 * 60


def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def to_unix_time(t):
    '''t is yyyyMMddhhmmss'''
    unix_time = 0

    year = int(t[0:4])
    month = int(t[4:6])
    day = int(t[6:8])
    hour = int(t[8:10])
    minute = int(t[10:12])
    second = int(t[12:14])

    if year >= 1970 and 0 < month < 13:
        for y in range(1970, year):
            unix_time += 365 * 24 * 60 * 60
            if (is_leap_year(y)):
                unix_time += 24 * 60 * 60
        for m in range(1, month):
            unix_time += MONTH_OF_DAYS[str(m)] * 24 * 60 * 60
        if month > 2 and is_leap_year(year):
            unix_time += 24 * 60 * 60
        for d in range(1, day):
            unix_time += 24 * 60 * 60
        for h in range(0, hour):
            unix_time += 60 * 60
        for m in range(0, minute):
            unix_time += 60
        unix_time += second
        unix_time_cn = unix_time - 8 * 60 * 60
        print 'unix time(china zone): ' + str(unix_time_cn)


def to_human_time(t):
    '''t is kind of this 1526039783'''
    # china zone time + 8 hour
    left_seconds = int(t) + 8 * 60 * 60
    year = 1970
    while True:
        if is_leap_year(year):
            year_seconds = LEAP_YEAR_OF_SECONDS
        else:
            year_seconds = YEAR_OF_SECONDS
        if left_seconds >= year_seconds:
            year += 1
            left_seconds -= year_seconds
        else:
            break
    print left_seconds
    month = 1
    if is_leap_year(year):
        month_days = MONTH_OF_DAYS_LEAP
    else:
        month_days = MONTH_OF_DAYS
    for m in range(1, 13):
        if left_seconds >= (month_days[str(m)] * 24 * 60 * 60):
            left_seconds -= month_days[str(m)] * 24 * 60 * 60
            month += 1
        else:
            break
    print month, left_seconds
    day = 1
    day_seconds = 24 * 60 * 60
    while True:
        if left_seconds >= day_seconds:
            day += 1
            left_seconds -= day_seconds
        else:
            break
    hour = 0
    hour_seconds = 60 * 60
    while True:
        if left_seconds >= hour_seconds:
            hour += 1
            left_seconds -= hour_seconds
        else:
            break
    minute = 0
    minute_seconds = 60
    while True:
        if left_seconds >= minute_seconds:
            minute += 1
            left_seconds -= minute_seconds
        else:
            break
    second = left_seconds

    print u"%4d年%02d月%02d日%02d时%02d分%02d秒 (GMT+8)" % (year, month, day, hour, minute, second)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "wrong parameters, just 3 is True"
    else:
        usage = sys.argv[1]
        t = sys.argv[2]
        if '-u' == usage:
            to_unix_time(t)
        if '-h' == usage:
            to_human_time(t)
