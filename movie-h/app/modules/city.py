from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class City(db.Model):
    id = Column(Integer,primary_key=True,nullable=False)
    city_id = Column(Integer,nullable=False)
    name = Column(String(64),nullable=False)
    spin = Column(String(64), nullable=False)


