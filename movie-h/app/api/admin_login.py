from .blueprint import admin_login
from flask import jsonify,request
from app.public.returnResponse import formats
from app.mysqls.admin_login import AdminLogin

@admin_login.route('/api/admin/login',methods=['POST'])
def admin_logins():
    run = AdminLogin()
    data = run.run(request.json)
    if data:
        return jsonify(formats('ok!',200,data))
    else:
        return jsonify(formats(run.prompt,300,[]))