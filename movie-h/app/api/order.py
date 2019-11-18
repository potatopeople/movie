from .blueprint import movie_order
from app.public.returnResponse import formats
from flask import jsonify,request
from app.mysqls.movie_order import MovieOrder
from threading import Lock


@movie_order.route('/api/movie/seat/order',methods=['PUT'])
def order():
    try:
        mutex = Lock()  # 创建锁
        mutex.acquire()  # 上锁
        pater = request.json
        data = MovieOrder()
        data = data.run(pater['data'],pater['token'])
        mutex.release() #解锁
        if data[0] == 2:
            return jsonify(formats('有座位已被购买', 300, data[1]))
        elif data[0] == 0:
            return jsonify(formats('OK!', 200, []))
        elif data[0] == 1:
            return jsonify(formats('订单建立失败!', 300, []))
        elif data[0] == 3:
            return jsonify(formats('您当前有未支付订单，无法购买!', 300, []))
        elif data[0] == 4:
            return jsonify(formats('用户信息错误！', 400, []))
    except Exception as e:
        return jsonify(formats('服务器响应失败', 500, e))