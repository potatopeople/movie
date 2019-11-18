from app.modules.admin import Admin,db as adb
import re
from app.mysqls.admin_data import DataQuery

class AdminData:

    prompt = ''

    @staticmethod
    def __check_token(token):
        basic = re.findall('Basic\s(.*)', token, re.S)[0]
        if basic:
            return basic
        else:
            return False

    @staticmethod
    def __verify_token(token):
        user = Admin.query.filter(
            Admin.token == token
        ).first()
        adb.session.close()
        if user:
            return True
        else:
            return False

    def run(self,token,types):
        token = self.__check_token(token)
        if token:
            if self.__verify_token(token):
                run = DataQuery()
                data = run.run(types)
                if data:
                    return data
                else:
                    self.prompt = '数据库异常'
                    return False
            else:
                self.prompt = '该用户无效'
                return False
        else:
            self.prompt = '请重新登录！'
            return False
