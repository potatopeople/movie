from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    id = Column(Integer, primary_key=True,nullable=False)
    username = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    avator = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)
