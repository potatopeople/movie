from app.modules.user import User
from app.public.user_token import Tokens

class UserData:
    data = {} # 返回给客户端的数据

    def __init__(self,username):
        self._select_user(username)

    def _select_user(self,username): #登录接口返回数据
        tokens = Tokens(username)
        result = User.query.filter(User.username == username).first()
        self.data['token'] = tokens.create_token
        self.data['userId'] = result.id
        self.data['name'] = result.name or ''
        self.data['sex'] = result.sex or ''
        self.data['avatar'] = result.avatar or ''
        self.data['email'] = result.email
        self.data['createDate'] = result.createDate

