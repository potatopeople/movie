from .blueprint import movie_seat
from app.public.returnResponse import formats
from flask import jsonify,request
from app.mysqls.query_seat import seat_data


@movie_seat.route('/api/movie/seat',methods=['POST'])
def seat():
    pater = request.json
    try:
        data = seat_data(pater['city_id'],pater['cinemas_id'],pater['movie_id'])
        return jsonify(formats('OK!', 200, data))
    except Exception as e:
        print(e,'参数错误')
        return jsonify(formats('参数错误!', 300, []))