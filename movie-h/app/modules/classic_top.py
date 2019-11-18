from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class ClassicTop(db.Model):
    id = Column(Integer,primary_key=True,nullable=False)
    rank = Column(Integer, nullable=False)
    name = Column(String(64), nullable=False)
    star = Column(String(64), nullable=False)
    score = Column(String(25), nullable=False)
    releaseTime = Column(String(64), nullable=False)
    img = Column(Text(0), nullable=False)
