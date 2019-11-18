from .blueprint import login
from flask import request,jsonify
from app.libs.login import verify_user
from app.public.returnResponse import formats
from app.dataFromats.login import UserData

@login.route('/api/login', methods=['POST'])
def userLogin():
    if verify_user(request.json):
        userData = UserData(request.json.get('username'))
        return jsonify(formats('登录成功！', 200, userData.data))
    else:
        return jsonify(formats('用户名或密码错误！', 300, {}))

