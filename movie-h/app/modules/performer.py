from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class MoviePerformer(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    vid = Column(Integer,nullable=False)
    img = Column(Text(0),nullable=False)
    catgory = Column(String(64),nullable=False)
    name = Column(String(64),nullable=False)
    sname = Column(String(64),nullable=True)
    value = Column(String(25))
