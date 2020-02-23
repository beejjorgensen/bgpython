import sys
import calendar

if len(sys.argv) != 3:
    print("usage: cal.py year month")
    sys.exit()

year = int(sys.argv[1])
month = int(sys.argv[2])

if month < 1 or month > 12:
    print("Month must be 1-12!")
    sys.exit()

calendar.prmonth(year, month)
