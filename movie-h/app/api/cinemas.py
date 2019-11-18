from .blueprint import cinemas
from app.public.returnResponse import formats
from flask import jsonify
from app.mysqls.cinemas_list import cinemas_list

@cinemas.route('/api/cinemas/cinemasList/<city_id>', methods=['GET'])
def cinemas_lists(city_id):
    try:
        if int(city_id):
            data = cinemas_list(int(city_id))
            return jsonify(formats('OK!', 200, data))
        else:
            return jsonify(formats('参数错误', 300, []))
    except Exception as e:
        print('参数错误',e)
        return jsonify(formats('参数错误', 300, []))
