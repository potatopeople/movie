from .blueprint import cinemas_movie
from app.public.returnResponse import formats
from flask import jsonify,request
from app.mysqls.cinemas_movie import movie_data


@cinemas_movie.route('/api/cinemas/cinemasList/movie', methods=['POST'])
def cinemasMoive():
    try:
        parameter = request.json
        data = movie_data(parameter['city_id'],parameter['cinemas_id'],parameter['money'])
        return jsonify(formats('OK!', 200, data))
    except Exception as e:
        print('参数错误',e)
        return jsonify(formats('参数错误', 300, []))