from database import session
from datetime import date
from tables import Holiday

def insert_holiday(holiday: Holiday) -> None:
    session.add(holiday)
    session.commit()

def is_holiday(date: date) -> bool:
    return session.query(Holiday.holi_date).filter_by(holi_date=date).count() > 0
