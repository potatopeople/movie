from .blueprint import query_talk
from flask import jsonify,request
from app.public.returnResponse import formats
from app.mysqls.query_talk import query_talks

@query_talk.route('/api/movie/get_talk',methods=['POST'])
def get_talk():
    try:
        pater = request.json
        data = query_talks(pater)
        if data:
            return jsonify(formats('ok!',200,data))
        elif data is False:
            return jsonify(formats('评论查询失败',500,[]))
        else:
            return jsonify(formats('没有此电影的评论', 300, []))
    except Exception as e:
        return jsonify(formats(e,500,[]))