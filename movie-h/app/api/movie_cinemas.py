from .blueprint import movie_cinemas
from app.public.returnResponse import formats
from flask import jsonify,request
from app.mysqls.movie_cinemas import query_cinemas

@movie_cinemas.route('/api/movie/cinemas_list', methods=['POST'])
def cinemas_list():
    request_data = request.json
    try:
        if int(request_data['movie_id']) and int(request_data['city_id']):
            data = query_cinemas(request_data['movie_id'],request_data['city_id'])
            return jsonify(formats('OK!', 200, data))
        else:
            return jsonify(formats('参数错误!', 200, []))
    except Exception as e:
        print(e)
        return jsonify(formats('/api/movie/cinemas_list，参数错误', 300, []))