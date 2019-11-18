from .blueprint import movie_search
from flask import request,jsonify
from app.public.returnResponse import formats
from app.mysqls.movie_search import MovieSearch

@movie_search.route('/api/movie/search',methods=['Post'])
def movieSearch():
    intro = request.json
    print(intro)
    if intro['keywords'] == '':
        return jsonify(formats('空值', 300, {}))
    elif 'keywords' and 'page' and 'pageSize' in intro.keys():
        data = MovieSearch(request.json)
        if data.run():
            return jsonify(formats('ok!', 200, data.data))
        else:
            return jsonify(formats(data.prompt, 300, {'data': []}))