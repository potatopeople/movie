import re
from app.mysqls.query_user import query_user

class VerifyToken:

    user = []
    token = ''
    prompt = ''
    user_infor = ''

    @staticmethod
    def __get_token(token):
        basic = re.findall('Basic\s(.*)', token, re.S)[0]
        if basic:
            return basic
        else:
            return False

    def check_filed(self,token): # 检查字段
        data = self.__get_token(token)
        if data:
            user = query_user('',data)
            return user
        else:
            return False


