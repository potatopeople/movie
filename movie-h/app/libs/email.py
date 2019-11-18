from app.http.send_email import post_email
from app.mysqls.email import check_email
from .. import cache

class EmailVerify:

    filed = ''
    user_email = ''
    type = ''
    prompt = ''
    caches = None

    def __init__(self, email):
        self.filed = email

    def type_prompt(self):
        if 'email' and 'type' in self.filed.keys():
            self.type = self.filed['type']
            self.user_email = self.filed['email']
            if self.type == 'createUser':
                if not check_email(self.filed['email']):
                    self.create_user()
                    return True
                else:
                    self.prompt = '该邮箱已被注册！'
                    return False
            else:
                self.prompt = '没有该验证类型'
                return False
        elif 'random' and 'email' in self.filed.keys():
            if self.verify_random():
                self.prompt = '验证成功！'
                return True
            else:
                self.prompt = '验证码错误！'
                return False
        else:
            self.prompt = '错误字段'
            return False

    def create_user(self):
        props = post_email(self.user_email)
        if props[1]:
            self.prompt = '发送成功！'
            prompt = {
                'email': self.user_email,
                'random': props[1]
            }
            cache.set(self.user_email, prompt, timeout=300)
        else:
            self.prompt = '抱歉！您的邮件发送失败，请重试'

    def verify_random(self):
        try:
            self.caches = cache.get(self.filed['email'])
            if str(self.caches['random']) == self.filed['random']:
                return True
            else:
                return False
        except TypeError:
            self.prompt = '验证码已过期，请重新发送邮件！'
            return False
