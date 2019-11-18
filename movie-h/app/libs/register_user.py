import re
from app.mysqls.create_user import CreateUser

class RegisUser:

    user_intro = dict
    field = ['email', 'username', 'password']
    prompt = ''
    name_reg = '^\w{7,10}$'
    passwd_reg = '^[^\s]{10,20}$'

    def __init__(self, data):
        self.user_intro = data

    def regis_user(self):
        if self.check_field():
            if self.check_effective():
                register = CreateUser(self.user_intro)
                props = register.register_user()
                if props == '成功':
                    self.prompt = '注册成功！'
                    return True
                elif props == '用户名重复':
                    self.prompt = '该用户名已存在'
                    return False
                elif props == '邮箱重复':
                    self.prompt = '该邮箱已被注册'
                    return False
                else:
                    self.prompt = '抱歉！注册失败，请重新注册'
                    return False
            else:
                return False
        else:
            self.prompt = '字段错误'
            return False

    def check_field(self):
        print(self.field,self.user_intro.keys())
        if self.field == list(self.user_intro.keys()):
            return True
        else:
            return False

    def check_effective(self):
        if re.findall(self.name_reg, self.user_intro['username']):
            if re.findall(self.passwd_reg, self.user_intro['password']):
                return True
            else:
                self.prompt = '密码格式错误'
                return False
        else:
            self.prompt = '用户名格式错误'
            return False
