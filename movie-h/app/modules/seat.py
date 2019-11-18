from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Seat(db.Model):
    id = Column(Integer,primary_key=True,nullable=False)
    city_id = Column(String(64), nullable=False)
    cinemas_id = Column(String(64), nullable=False)
    movie_id = Column(String(64), nullable=False)
    row = Column(Integer, nullable=False)
    clumn = Column(Integer, nullable=False)
    chose = Column(Integer, nullable=False,default=0)
