from database import session
from tables import Holiday

# データを取得する,追加した情報を参照するだけ。実行する。
holidaylist=session.query(Holiday).filter_by(holi_date="")

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)

