from .blueprint import movie_list
from flask import request, jsonify
from app.public.returnResponse import formats
from app.libs.movie_list import MovieList


@movie_list.route('/api/movie',methods=['POST'])
def movie_data():
    movie = MovieList(request.json)
    if movie.verify_filed():
        return jsonify(formats(movie.prompt, 200, movie.data))
    else:
        return jsonify(formats(movie.prompt, 300, {}))
