# Enter your code here. Read input from STDIN. Print output to STDOUT

# The calendar module allows you to output calendars and provides additional useful functions for them./

import calendar
month, day, year = map(int, input("Enter the date(12 03 2024) :").split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())