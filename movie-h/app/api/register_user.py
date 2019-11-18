from .blueprint import register_user
from flask import request,jsonify
from app.public.returnResponse import formats
from app.libs.register_user import RegisUser

@register_user.route('/api/registerUser', methods=['POST'])
def create_user():
    register = RegisUser(request.json)
    if register.regis_user():
        return jsonify(formats(register.prompt, 200, {}))
    else:
        return jsonify(formats(register.prompt, 300, {}))