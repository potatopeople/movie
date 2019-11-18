from .blueprint import address
from app.public.returnResponse import formats
from flask import jsonify
from app.mysqls.address import city_data

@address.route('/api/address', methods=['GET'])
def query_address():
    data = city_data()
    if isinstance(data,dict):
        return jsonify(formats('OK!', 200, data))
    else:
        return jsonify(formats('请求错误!', 300, []))