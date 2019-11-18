from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CinemasMovie(db.Model):
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String(64), nullable=False)
    score = Column(String(64), nullable=False)
    play_time = Column(String(64), nullable=False)
    catgory = Column(String(64), nullable=False)
    star = Column(String(64), nullable=False)
    lang = Column(String(64), nullable=False)
    city_id = Column(Integer, nullable=False)
    cinemas_id = Column(Integer, nullable=False)
    movie_id = Column(String(64), nullable=False)
    movie_img = Column(Text, nullable=False)
    cinemas_img = Column(Text, nullable=True)
    seat = Column(String(255), nullable=False)
    money = Column(Integer,nullable=True)
    room = Column(String(255),nullable=True)