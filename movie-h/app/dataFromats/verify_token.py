from app.modules.user import User

class UserData:
    data = {} # 返回给客户端的数据

    def __init__(self,username):
        self._select_users(username)

    def _select_users(self,username):
        result = User.query.filter(User.username == username).first()
        self.data['userId'] = result.id
        self.data['name'] = result.name or ''
        self.data['sex'] = result.sex or ''
        self.data['avatar'] = result.avatar or ''
        self.data['email'] = result.email
        self.data['createDate'] = result.createDate
