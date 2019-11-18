from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SeatOrder(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    sid = Column(Integer, nullable=False)
    id_card = Column(String(255), nullable=True)
    buy_date = Column(String(64), nullable=False)
    phone = Column(String(64),nullable=False)
    tf = Column(String(25),nullable=False)
    batch = Column(String(255),nullable=False)
