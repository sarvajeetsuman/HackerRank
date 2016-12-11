#https://www.hackerrank.com/challenges/calendar-module

import calendar
lst = list(input().split())
print((calendar.day_name[calendar.weekday(int(lst[2]),int(lst[0]),int(lst[1]))]).upper())
