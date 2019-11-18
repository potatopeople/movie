from .blueprint import get_order
from app.public.returnResponse import formats
from flask import jsonify,request
from app.libs.order_handel import OrderHandel


@get_order.route('/api/movie/seat/order/get_order',methods=['GET'])
def get_user_order():
    try:
        orders = OrderHandel()
        data = orders.run(request.headers.get('Authorization'),request.args['type'],request.args['date'])
        if data:
            return jsonify(formats('ok!', 200, data))
        else:
            return jsonify(formats(orders.prompt, 300, []))
    except Exception as e:
        print(e)
        return jsonify(formats('客户端错误！', 400, []))