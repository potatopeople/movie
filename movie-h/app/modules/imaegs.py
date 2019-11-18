from sqlalchemy import Column,Integer,Text
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class MovieImages(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    vid = Column(Integer,nullable=True)
    img = Column(Text(0),nullable=True)
