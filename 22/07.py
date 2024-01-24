from math import pi, sin
import datetime as dt


def rhythm_value(period_length):
    return str(round(sin((2 * pi * period.days) / period_length) * 100, 2))


date1 = input().split(".")
date2 = input().split(".")
date_of_birth = dt.date(int(date1[2]), int(date1[1]), int(date1[0]))
date_of_count = dt.date(int(date2[2]), int(date2[1]), int(date2[0]))
period = date_of_count - date_of_birth

print(rhythm_value(23) + "\n" + rhythm_value(28) + "\n" + rhythm_value(33))

