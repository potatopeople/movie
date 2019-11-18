from .blueprint import movie_top
from flask import jsonify,request
from app.public.returnResponse import formats
from app.libs.movie_top import MovieTop


@movie_top.route('/api/movieTop', methods=['POST'])
def movie_data_top():
    run = MovieTop(request.json)
    if run.verify():
        return jsonify(formats(run.prompt, 200, run.data))
    else:
        return jsonify(formats(run.prompt, 300, {}))