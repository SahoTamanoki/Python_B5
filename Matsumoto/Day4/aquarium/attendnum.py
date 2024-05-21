from database import session
from datetime import date
from tables import Attendnum

def insert_attendnum(entry_date: date, adult: int, child: int) -> None:
    seq = session.query(Attendnum.seq).filter_by(date=entry_date).count()
    if seq > 0:
        seq += 1
    else:
        seq = 1
    
    attendnum = Attendnum(date=entry_date, seq=seq, adult=adult, child=child)
    session.add(attendnum)
    session.commit()
