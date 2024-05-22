from database import session
from tables import Holiday

# データを取得する
holidaylist=session.query(Holiday).filter_by(holi_date= args[1])

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)
