from sqlalchemy import create_engine
from flask import current_app
from sqlalchemy.orm import sessionmaker
import time
from app.modules.user import User


class CreateUser:

    user_intro = None

    def __init__(self, data):
        self.user_intro = data

    def register_user(self):
        engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
        Session = sessionmaker(bind = engine)
        session = Session()
        findex = session.query(User).filter(
            User.username == self.user_intro['username']
        ).all()
        if not findex:
            findex = session.query(User).filter(
                User.email == self.user_intro['email']
            ).all()
            if not findex:
                obj = User(
                    username=self.user_intro['username'],
                    password=self.user_intro['password'],
                    email=self.user_intro['email'],
                    createDate=int(time.time())
                )
                session.add(obj)  # 添加
                try:
                    print('注册')
                    session.commit()  # 提交
                except Exception as e:
                    print(e)
                    session.rollback()  # 回滚
                    return False
                else:
                    return '成功'
                finally:
                    session.close()  # 关闭
            else:
                return '邮箱重复'
        else:
            return '用户名重复'