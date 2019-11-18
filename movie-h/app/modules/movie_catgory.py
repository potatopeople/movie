from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MovieCatgory(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    catgory = Column(String(64),nullable=True)
    years = Column(String(64),nullable=True)
    region = Column(String(64),nullable=True)

