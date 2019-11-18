from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(25),nullable=False,unique=True)
    name = Column(String(10),nullable=True)
    sex = Column(String(1),nullable=True)
    avatar = Column(Text(0),nullable=True,default='https://img.meituan.net/maoyanuser/da1d6e35eda3d36bd7c61a60ea7f942a10407.png')
    token = Column(String(255),nullable=True)

    # @property
    # def password(self):
    #     raise AttributeError('明文密码不可读')
    #
    # #密码加密
    # @password.setter
    # def password(self, value):
    #     self.passwords = generate_password_hash(value)
    #
    # #密码验证
    # def check_login_password(self, password):
    #     return check_password_hash(self.passwords, password)
