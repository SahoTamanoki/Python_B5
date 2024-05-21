from datetime import date
from database import session
from tables import Holiday


#テーブル：Attendnumの定義
class Attendnum(Base):
    __tablename__ = 'attendnum'
    date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)    
    child = Column('child', Integer) 
    