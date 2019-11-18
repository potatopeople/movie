from app.modules.admin import Admin,db as adb


class AdminLogin:

    prompt = ''

    @staticmethod
    def __token_check(datas):
        if 'token' in datas.keys():
            return True
        else:
            return False

    def __query_token(self,token):
        user = Admin.query.filter(
            Admin.token == token
        ).first()
        adb.session.close()
        anchor = {'name': user.name, 'token': user.token}
        return anchor

    @staticmethod
    def __query_username(username,password):
        user = Admin.query.filter(
            Admin.username == username,
            Admin.password == password
        ).first()
        adb.session.close()
        if user:
            anchor = {'name':user.name,'token':user.token}
            return anchor
        else:
            return False

    def run(self,datas):
        if self.__token_check(datas):
            data = self.__query_token(datas['token'])
            if data:
                return data
            else:
                self.prompt = '账户错误'
                return False
        else:
            data = self.__query_username(datas['username'],datas['password'])
            return data