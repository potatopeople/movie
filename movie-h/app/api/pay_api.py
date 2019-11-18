from .blueprint import pay_api
from app.public.returnResponse import formats
from flask import jsonify,request
from app.http.zhi_fu_bao import run


@pay_api.route('/api/movie/pay',methods=['PUT'])
def pay_apis():
    try:
        pater = request.json
        url = run(pater['money'],pater['batch'],pater['id_card'])
        if url:
            return jsonify(formats('ok!', 200, url))
        else:
            return jsonify(formats('error!', 300, '订单已过期'))
    except Exception as e:
        return jsonify(formats('error!', 500, e))