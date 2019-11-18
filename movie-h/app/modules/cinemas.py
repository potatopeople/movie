from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cinemas(db.Model):
    id = Column(Integer, primary_key=True,nullable=False)
    city_id = Column(Integer, nullable=False)
    cinemas_id = Column(Integer, nullable=False)
    name = Column(String(64), nullable=False)
    address = Column(String(255), nullable=False)
    money = Column(Integer, nullable=False)
