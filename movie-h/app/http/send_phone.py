import requests
import random
import json
from .. import cache
from app.mysqls.add_user import AddUser
from app.mysqls.query_user import query_user

class SendPhone:
    headers = {"Authorization":'APPCODE a0e1d3c9ab134e67a94413cb4c96cc72'}
    tpl_id = 47331
    sign = '网极科技'
    prompt = ''
    token = ''

    def __send_code(self,code,phone):
        response = requests.get(
            url= 'https://smsapi.api51.cn/single_sms_get/',
            params= {
                'mobile': phone,
                'params': '用户,%s'%code,
                'sign': self.sign,
                'tpl_id': self.tpl_id
            },
            headers=self.headers
        )
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return 'false'

    @staticmethod
    def __code_cache(phone,code): #缓存code
        data = {
            'phone': phone,
            'code': code
        }
        cache.set(phone, data, timeout=180)

    @staticmethod
    def __create_code():
        code = "".join(random.sample('0123456789', 5)) #随机数
        return code

    def __verify_code(self,phone,code):
        try:
            data = cache.get(phone)
            if data['code'] == code:
                user = query_user(phone)
                return user
            elif not data:
                self.prompt = '请发送验证码'
                return False
            else:
                self.prompt = '验证码错误'
                return False
        except TypeError:
            self.prompt = '验证码已过期，请重新发送'
            return False

    def __add_user(self,phone):
        user = AddUser()
        token = user.run(phone)
        self.token = token

    def __type_check(self,phone, types, ccode):
        if types == 'send':
            code = self.__create_code()
            pater = self.__send_code(code, phone)
            if pater == 'false':
                self.prompt = '短信发送失败'
                return False
            else:
                if pater["errmsg"] == 'OK':
                    self.__code_cache(phone, code)
                    self.__add_user(phone)
                    return code
                else:
                    self.prompt = pater["errmsg"]
                    return False
        elif types == 'verify':
            data = self.__verify_code(phone,ccode)
            if data:
                return data
            else:
                return False

    def run(self, phone, types, code):
        return self.__type_check(phone, types,code)
