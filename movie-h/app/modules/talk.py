from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class MovieTalk(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    mid = Column(Integer,nullable=False)
    cat = Column(String(25),nullable=False)
    username = Column(String(64),nullable=False)
    main = Column(Text(0),nullable=False)
    time = Column(String(64),nullable=False)
