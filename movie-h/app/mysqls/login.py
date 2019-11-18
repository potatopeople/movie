from sqlalchemy import create_engine
from flask import current_app
from sqlalchemy.orm import sessionmaker
from app.modules.user import User

class Login:
    _username = '' #用户名
    _password = '' #用户密码

    def __init__(self, data):
        Login._username = data
        self._select_user()

    @classmethod
    def _select_user(cls):
        engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
        Session = sessionmaker(bind = engine)
        session = Session()
        res_filter = session.query(User).filter(User.username== cls._username).first()
        cls._password = res_filter
        session.close()

    @property
    def password(self):
        return Login._password




