from datetime import date, datetime, timedelta
from database import session
from tables import Holiday
import jpholiday

def InsertHoliday():
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)

    current_date = start_date
    while current_date <= end_date:
        if jpholiday.is_holiday(current_date):
            holidays = [current_date, jpholiday.is_holiday_name(datetime.date(current_date))]
            session.add(holidays)
            session.commit()
        current_date += timedelta(days=1)

    return current_date


print(InsertHoliday())

# def HolidayCheck(date):    
#     dt = datetime.strptime(date, "%Y%m%d")
#     weekday = dt.weekday()
#     if weekday > 4 or InsertHoliday(dt) == True:
#         fee = adult * 2400 + child * 1500

#     else:
#         fee = adult * 2000 + child * 1200

# args = sys.argv

# date = str(arg[1])
# adult = int(arg[2])
# child = int(arg[3])

