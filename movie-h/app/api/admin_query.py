from  .blueprint import admin_query
from flask import jsonify,request
from app.public.returnResponse import formats
from app.libs.admin_data import AdminData

@admin_query.route('/api/admin/data_query/<types>',methods=['GET'])
def query_data(types):
    try:
        run = AdminData()
        data = run.run(request.headers.get('Authorization'), types)
        if data:
            return jsonify(formats('ok!',200,data))
        else:
            return jsonify(formats(run.prompt, 300, []))
    except Exception as e:
        return jsonify(formats(e, 500, []))