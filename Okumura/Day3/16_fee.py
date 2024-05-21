arg = [ "python aquacalc.py",20220521,1,2]

date = str(arg[1])
adult = int(arg[2])
child = int(arg[3])

from datetime import datetime


try:
    dt = datetime.strptime(date, "%Y%m%d")
    weekday = dt.weekday()
    if weekday < 5:
        fee = adult * 2000 + child * 1200
    else:
        fee = adult * 2400 + child * 1500
except ValueError:
    print("無効な日付形式です。正しい形式で入力してください。")

print(fee,end="")