from .blueprint import save_user
from flask import jsonify,request
from app.public.returnResponse import formats
from app.mysqls.change_user import changes_data

@save_user.route('/api/user/save',methods=['POST'])
def change_data():
    try:
        pater = request.json
        token = request.headers.get('Authorization')
        data = changes_data(token,pater)
        if data:
            return jsonify(formats('ok!', 200, data))
        else:
            return jsonify(formats('服务器错误!', 500, []))
    except Exception as e:
        return jsonify(formats(e, 500, []))
