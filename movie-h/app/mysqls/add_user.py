from app.modules.user import User,db as udb
import random

class AddUser:

    user = '' #用户信息
    token = ''

    def __check_user(self, phone):
        user = User.query.filter(User.username == phone).all()
        udb.session.close()
        if len(user):
            self.user = user
            return True #有
        else:
            return False#没有

    def __get_user_token(self):
        for item in self.user:
            return item.token

    @staticmethod
    def __set_token(phone): #设置token
        token = ''
        for item in phone:
            num = "".join(random.sample('!@#$%^&*', 1))
            token = token + num + item
        return token

    def __add_user(self,phone): #添加用户
        token = self.__set_token(phone)
        user = User(username=phone,token=token,name='无名氏')
        udb.session.add(user)
        udb.session.commit()
        udb.session.close()
        return token

    def run(self, phone):
        if self.__check_user(phone):
            return self.__get_user_token()
        else:
            return self.__add_user(phone)