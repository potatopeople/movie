from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class SoonMovie(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    sid = Column(Integer, nullable=False)
    name = Column(String(64), nullable=False)
    elname = Column(String(255))
    img = Column(Text(0), nullable=False)
    cat = Column(String(64), nullable=True)
    catgory = Column(String(64), nullable=True)
    address = Column(String(64), nullable=True)
    playTime = Column(String(64), nullable=True)
    releaseTime = Column(String(64), nullable=True)
    ticketRank = Column(String(25),nullable=True)
    introduction = Column(Text(0), nullable=True)
    people = Column(Integer,nullable=True)
    play_cat = Column(String(255), nullable=False)
