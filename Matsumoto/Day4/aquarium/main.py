from attendnum import insert_attendnum
from datetime import date
import holiday
import sys

args = sys.argv

input_date = args[1]
adult = int(args[2])
child = int(args[3])

dt = date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
insert_attendnum(dt, adult, child)

if dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun" or holiday.is_holiday(dt):
    pay = 2400 * adult + 1500 * child
else:
    pay = 2000 * adult + 1200 * child

print(pay)
