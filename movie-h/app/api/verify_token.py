from .blueprint import verify_token
from flask import request, jsonify
from app.public.returnResponse import formats
from app.libs.verify_user_token import VerifyToken


@verify_token.route('/api/user/verifyToken',methods=['GET'])
def verifyToken():
    try:
        verify = VerifyToken()
        user = verify.check_filed(request.headers.get('Authorization'))
        if user:
            return jsonify(formats('ok',200,user))
        else:
            return jsonify(formats('请重新登录',300,[]))
    except Exception as e:
        return jsonify(formats(e, 500, []))