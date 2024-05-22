#引数の設定
from database import session
from tables import Holiday

import sys
args = sys.argv
year = int(args[1][0:4])
month = int(args[1][4:6])
day = int(args[1][6:8])
count_adult = int(args[2])
count_child = int(args[3])

#曜日判定のモジュールインポート
import datetime
t = datetime.date(year,month,day)
wkd = t.weekday()

#各日にちの料金設定
price_workday = {"大人":2000, "子供":1200}
price_holiday = {"大人":2400, "子供":1500}

#処理開始
if 0<= wkd <= 4 or t == Holiday.holi_date:
    total = count_adult * price_workday["大人"] + count_child * price_workday["子供"]
elif wkd == 5 or wkd == 6:
    total = count_adult * price_holiday["大人"] + count_child * price_holiday["子供"]
print(total,end="") 