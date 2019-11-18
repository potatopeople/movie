import re
from app.modules.user import User,db as udb
from app.mysqls.add_talk import add_talk

class SendTalk:

    prompt = '发送失败！'

    @staticmethod
    def __verify_token(token):
        basic = re.findall('Basic\s(.*)', token, re.S)[0]
        if basic:
            return basic
        else:
            return False

    @staticmethod
    def __query_user(token):
        user = User.query.filter(
            User.token == token
        ).first()
        udb.session.close()
        if user:
            return user.username
        else:
            return False

    def run(self,token,datas):
        token = self.__verify_token(token)
        if token:
            name = self.__query_user(token)
            if name:
                tf = add_talk(name,datas)
                return tf
            else:
                self.prompt = '没有该用户！'
                return False
        else:
            self.prompt = '请登录后评论'
            return False