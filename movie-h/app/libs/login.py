from app.mysqls.login import Login
from app.filed.login import UserIntro

def verify_user(filed):

    user = UserIntro()
    if user.usernames and user.passwords in filed.keys(): # 是否有这两个字段
        login = Login(filed['username'])
        if login.password:
            user = login.password
            return True if user.check_login_password(filed['passwords']) else False
        else:
            return False
    else:
        return False
