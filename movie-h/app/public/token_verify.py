class TokenVerify:

    user = [] #用户token信息

    def __init__(self, userObj):
        self.add_token(userObj)

    @classmethod
    def add_token(cls,userObj):
        if not cls.user:
            cls.user.append(userObj)
        else:
            for i,user in enumerate(cls.user):
                if userObj['username'] == user['username']:
                    cls.user[i] = userObj #重复就覆盖
                elif i == len(cls.user) - 1:
                    cls.user.append(userObj) # 否则就添加
        print('所有用户信息：', cls.user)
