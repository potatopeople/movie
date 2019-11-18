from .blueprint import movie_catgory
from flask import jsonify
from app.public.returnResponse import formats
from app.mysqls.movie_catgory import getData


@movie_catgory.route('/api/movieCatgory',methods=['GET'])
def movieCatgory():
    return jsonify(formats('OK!', getData()[0], getData()[1]))